import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow
from PyQt6.uic import loadUi

class Calculator(QWidget):
    
    def __init__(self, parent=None):
        self.output_str = ""
        super(Calculator, self).__init__(parent)
        loadUi("calculator.ui", self)
        self.one.clicked.connect(lambda: self.setOutput('1'))
        self.two.clicked.connect(lambda: self.setOutput('2'))
        self.three.clicked.connect(lambda: self.setOutput('3'))
        self.four.clicked.connect(lambda: self.setOutput('4'))
        self.five.clicked.connect(lambda: self.setOutput('5'))
        self.six.clicked.connect(lambda: self.setOutput('6'))
        self.seven.clicked.connect(lambda: self.setOutput('7'))
        self.eight.clicked.connect(lambda: self.setOutput('8'))
        self.nine.clicked.connect(lambda: self.setOutput('9'))
        self.zero.clicked.connect(lambda: self.setOutput('0'))
        self.dot.clicked.connect(lambda: self.setOutput('.'))
        
        #Operation Buttons
        self.addition.clicked.connect(lambda: self.setOutput('+'))
        self.minus.clicked.connect(lambda: self.setOutput('-'))
        self.multiply.clicked.connect(lambda: self.setOutput('x'))
        self.divide.clicked.connect(lambda: self.setOutput('÷'))
        
        #Delete ALl
        self.deleteAll.clicked.connect(self.delete)
        
        #Show the answer
        self.equal.clicked.connect(self.showAnswer)
        
    def showAnswer(self):
        try:
            formattedAns = self.output_str.replace("x", "*").replace("÷", "/")
            ans = eval(formattedAns)
            self.output_str = str(ans)  
        except SyntaxError:
            QMessageBox.warning(self, "Error", "Invalid syntax")
        else:
            self.output.setText(str(ans))
            self.opOutput.setText("")
            
    
    def showInitialAnswer(self):
        try:
            formattedAns = self.output_str.replace("x", "*").replace("÷", "/")
            ans = eval(formattedAns)
            if '+' in self.output_str or '-' in self.output_str or 'x' in self.output_str or '÷' in self.output_str:
                self.opOutput.setText(str(ans)) 
        except SyntaxError:
            pass
        
               
    
    def delete(self):
        self.output_str = ""
        self.opOutput.setText("")
        self.output.setText("0")    
        
    def updateOutput(self):
        self.output.setText(self.output_str)
        
    def setOutput(self, num):
        self.output_str += num
        self.updateOutput()
        self.showInitialAnswer()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
        