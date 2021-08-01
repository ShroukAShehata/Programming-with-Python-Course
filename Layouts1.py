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
        mainlayout = QVBoxLayout()
        toplayout = QVBoxLayout()
        bottomlayout = QHBoxLayout()

        label1 = QLabel("Future Career Camp", self)
        label2 = QLabel("Programming with python track", self)
        check1 = QC("Group 4",self)

        btn1 = QPushButton("submit",self)
        btn2 = QPushButton("exit",self)

        mainlayout.addLayout(toplayout)
        mainlayout.addLayout(bottomlayout)

        toplayout.addStretch()
        toplayout.addWidget(label1)
        toplayout.addStretch()
        toplayout.addWidget(label2)
        toplayout.addStretch()
        toplayout.addWidget(check1)
        toplayout.addStretch()


        bottomlayout.addWidget(btn1)
        bottomlayout.addWidget(btn2)

        self.setLayout(mainlayout)
        self.show

app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()
