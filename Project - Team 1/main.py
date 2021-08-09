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
        self.setWindowTitle("Camp Application")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.Layouts()
        self.show()

    def UI(self):
        self.studentslist = QListWidget()
        self.btnNew = QPushButton("New")
        self.btnDelete = QPushButton("Delete")

    def Layouts(self):
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QHBoxLayout()

        self.rightLayout.addLayout(self.topLayout)
        self.rightLayout.addLayout(self.bottomLayout)
        self.mainLayout.addLayout(self.leftLayout , 40)
        self.mainLayout.addLayout(self.rightLayout , 60)

        self.topLayout.addWidget(self.studentslist)
        self.bottomLayout.addWidget(self.btnNew)
        self.bottomLayout.addWidget(self.btnDelete)

        self.setLayout(self.mainLayout)
        self.show()












app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()
