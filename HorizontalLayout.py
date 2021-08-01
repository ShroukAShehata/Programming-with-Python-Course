import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os

class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("HorizontalBox Layout")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.show()

    def UI(self):
        #hbox1 = QHBoxLayout()

        btn1 = QPushButton("submit",self)

        btn2 = QPushButton("exit",self)
        btn2.move(80,0)


        #hbox1.addStretch()
        #hbox1.addWidget(btn1)
        #hbox1.addWidget(btn2)
        #hbox1.addStretch()

        #self.setLayout(hbox1)
        #self.show()


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()