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
        self.show()

    def UI(self):
        formLayout = QFormLayout()

        label1 = QLabel("Name :",self)
        label2 = QLabel("Mail :",self)
        label3 = QLabel("Mobile :",self)
        label4 = QLabel("Password :", self)
        label5 = QLabel("Track :", self)
        label6 = QLabel("Group :", self)
        label7 = QLabel("Why you want to apply :", self)

        nametext = QLineEdit(self)
        nametext.setPlaceholderText("Enter your name")
        mobiletext = QLineEdit(self)
        mobiletext.setPlaceholderText("Enter your mobile")
        mailtext = QLineEdit(self)
        mailtext.setPlaceholderText("Enter your email")
        passwordtext = QLineEdit(self)
        passwordtext.setPlaceholderText("Enter your password")
        passwordtext.setEchoMode(QLineEdit.Password)
        mailtext.setEchoMode(QLineEdit.Password)

        track = QComboBox(self)
        track.addItems(["Programming with Python", "Web Design", "Networks", "Marketing"])

        group = QSpinBox(self)
        group.setRange(1, 5)
        group.setSuffix(" grp")

        whytext = QTextEdit(self)
        whytext.setPlaceholderText("Tell us why you want to apply")

        malegender = QRadioButton("Male", self)
        femalegender = QRadioButton("Female", self)

        submitbutton = QPushButton("Submit", self)
        exitbutton = QPushButton("Exit", self)

        formLayout.addRow(label1,nametext)
        formLayout.addRow(label2, mailtext)
        formLayout.addRow(label3, mobiletext)
        formLayout.addRow(label4, passwordtext)
        formLayout.addRow(label5, track)
        formLayout.addRow(label6, group)
        formLayout.addRow(label7, whytext)
        formLayout.addRow(malegender, femalegender)
        formLayout.addRow(submitbutton, exitbutton)

        self.setLayout(formLayout)
        self.show()


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()
