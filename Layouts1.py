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
        check1 = QCheckBox("Group 4",self)
        self.label3 = QLabel("null",self)

        btn1 = QPushButton("submit",self)
        btn1.clicked.connect(self.first)
        btn2 = QPushButton("exit",self)
        btn2.clicked.connect(self.second)

        mainlayout.addLayout(toplayout)
        mainlayout.addLayout(bottomlayout)

        toplayout.addStretch()
        toplayout.addWidget(label1)
        toplayout.addStretch()
        toplayout.addWidget(label2)
        toplayout.addStretch()
        toplayout.addWidget(check1)
        toplayout.addStretch()
        toplayout.addWidget(self.label3)
        toplayout.addStretch()


        bottomlayout.addWidget(btn1)
        bottomlayout.addWidget(btn2)

        self.setLayout(mainlayout)
        self.show

    def first(self):
        #print("You pressed submit")
        self.label3.setText("You pressed submit")

    def second(self):
        #print("You pressed exit")
        self.label3.setText("You pressed exit")


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()
