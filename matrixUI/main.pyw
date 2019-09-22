# https://pythonprogramminglanguage.com/pyqt5-hello-world/
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QTextEdit
from PyQt5 import uic
from matrix import *

class HelloWindow(QMainWindow):
    def __init__(self):
        super(HelloWindow, self).__init__()
        self.ui = uic.loadUi('main.ui', self)
        self.ui.calcButton.clicked.connect(self.calculate)

    def calculate(self):
        text = self.ui.inputMatrix.toPlainText()
        l = text.split('\n')
        m = initMatrixFromText(l)
        self.ui.outputMatrix.setText('Original matrix is')
        self.ui.outputMatrix.append(str(m))
        self.ui.outputMatrix.append('Transposed matrix is')
        self.ui.outputMatrix.append(str(m.transpose()))
        self.ui.outputMatrix.append(f'Determinant is {m.determinant()}')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )
