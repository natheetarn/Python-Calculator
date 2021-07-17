from PyQt5 import QtWidgets
from cal import Ui_MainWindow


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        
        super().__init__()

        self.operator = ''
        self.negative = False
        self.which_string = 1
        self.repeat = 0

        self.displayString = ""
        self.displayString2 = ""

        self.setupUi(self)
        self.button0.clicked.connect(self.clicked)
        self.button1.clicked.connect(self.clicked)
        self.button2.clicked.connect(self.clicked)
        self.button3.clicked.connect(self.clicked)
        self.button4.clicked.connect(self.clicked)
        self.button5.clicked.connect(self.clicked)
        self.button6.clicked.connect(self.clicked)
        self.button7.clicked.connect(self.clicked)
        self.button8.clicked.connect(self.clicked)
        self.button9.clicked.connect(self.clicked)
        self.dotButton.clicked.connect(self.clicked)
        self.plusButton.clicked.connect(self.clicked)
        self.minusButton.clicked.connect(self.clicked)
        self.multiplyButton.clicked.connect(self.clicked)
        self.divideButton.clicked.connect(self.clicked)
        self.equalButton.clicked.connect(self.clicked)
        self.DELButton.clicked.connect(self.clicked)
        self.ACButton.clicked.connect(self.clicked)
        self.plusMinusButton.clicked.connect(self.clicked)
        
    def clicked(self):
        sender = self.sender()
        if sender.text() in ['+','-','x','/']:
            self.operator = sender.text()
            self.which_string = 2
        elif sender.text() == "=":
            self.operation()
        elif sender.text() == '+/-':
            self.setNegative()
        elif sender.text() =='.':
            self.deci()
        elif sender.text() == "DEL":
            self.DEL()
        elif sender.text() == "AC":
            self.AC()
        elif sender.text() in ['1','2','3','4','5','6','7','8','9','0']:
            self.strAppender()
        
        

    def strAppender(self):
        sender = self.sender()
        if self.repeat == 0 and self.which_string == 1:
            self.displayString += sender.text()
            self.label.setText(self.displayString)
        elif self.repeat == 0 and self.which_string == 2:
            self.displayString2 += sender.text()
            self.label.setText(self.displayString2)
        elif self.repeat == 1:
            self.displayString ="" + sender.text()
            self.repeat = 0
            self.label.setText(self.displayString)
        
        

    def operation(self):
        self.which_string = 1
        if self.displayString2 != "" and self.displayString != "":
            
            if self.operator == '+':
                self.label.setText((str(float(self.displayString) + float(self.displayString2))))
                
            elif self.operator == '-':
                self.label.setText((str(float(self.displayString) - float(self.displayString2))))
                
            elif self.operator == 'x':
                self.label.setText((str(float(self.displayString) * float(self.displayString2))))
            
            elif self.operator == '/':
                self.label.setText((str(float(self.displayString) / float(self.displayString2))))
        
        self.displayString = ""
        self.displayString2 = ""
        
    
    def deci(self):
        sender = self.sender()
        if self.which_string == 1:
            if '.' in self.label.text():
                print("ERROR CANT ADD MORE DECIMAL")
            else:
                self.displayString += sender.text()
                self.label.setText(self.displayString)
        elif self.which_string == 2:
            if '.' in self.label.text():
                print("ERROR CANT ADD MORE DECIMAL")
            else:
                self.displayString2 += sender.text() 
                self.label.setText(self.displayString2)

            

    def DEL(self):
        if self.which_string == 1:
            self.displayString = self.displayString[0:-1]
            self.label.setText(self.displayString)
            
        elif self.which_string == 2:
            self.displayString2 = self.displayString2[0:-1]
            self.label.setText(self.displayString2)
    
    def AC(self):
        self.displayString2 = ""
        self.displayString = ""
        self.which_string = 1
        self.negative = False
        self.operator = ""

        self.label.setText("")
            

    
    def setNegative(self):
        if self.negative:
            self.negative = False
            if self.which_string == 1:
                self.displayString = self.displayString[1:]
                self.label.setText(self.displayString)
            elif self.which_string == 2:
                self.displayString2 = self.displayString2[1:]
                self.label.setText(self.displayString2)
            
        else:
            self.negative = True
            if self.which_string == 1:
                self.displayString = "-" + self.displayString
                self.label.setText(self.displayString)
            elif self.which_string == 2:
                self.displayString2 = "-" + self.displayString2
                self.label.setText(self.displayString2)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Calculator()
    MainWindow.show()
    sys.exit(app.exec_())

    