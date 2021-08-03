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
        vbox1 = QVBoxLayout()

        list = QListWidget(self)
        items=["Maths","IT","Electricity"]
        list.addItems(items)
        btn1 = QPushButton("submit",self)
        btn2 = QPushButton("exit",self)


        vbox1.addWidget(list)
        vbox1.addStretch()
        vbox1.addWidget(btn1)
        vbox1.addWidget(btn2)
        vbox1.addStretch()

        self.setLayout(vbox1)
        self.show()


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()