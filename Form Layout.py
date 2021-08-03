import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import sqlite3

con = sqlite3.connect("firstdatabase.db")
cursor = con.cursor()

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
        label4 = QLabel("ID :", self)


        self.nametext = QLineEdit(self)
        self.nametext.setPlaceholderText("Enter your name")
        self.mobiletext = QLineEdit(self)
        self.mobiletext.setPlaceholderText("Enter your mobile")
        self.mailtext = QLineEdit(self)
        self.mailtext.setPlaceholderText("Enter your email")
        self.idtext = QLineEdit(self)
        self.idtext.setPlaceholderText("Enter your ID")




        submitbutton = QPushButton("Submit", self)
        submitbutton.clicked.connect(self.getvalues)
        exitbutton = QPushButton("Exit", self)
        exitbutton.clicked.connect(self.checkexit)

        formLayout.addRow(label1,self.nametext)
        formLayout.addRow(label2, self.mailtext)
        formLayout.addRow(label3, self.mobiletext)
        formLayout.addRow(label4, self.idtext)
        formLayout.addRow(submitbutton, exitbutton)

        self.setLayout(formLayout)
        self.show()

    def getvalues(self):
        name = self.nametext.text()
        mail = self.mailtext.text()
        mobile = self.mobiletext.text()
        id = self.idtext.text()
        cursor.execute("INSERT INTO Students VALUES(?,?,?,?)",(name,id,mail,mobile) )
        con.commit()
        print("Done")

    def checkexit(self):
        mbox = QMessageBox.question(self,"Warning!","Are you sure you want to exit?",QMessageBox.Yes | QMessageBox.No )
        if mbox==QMessageBox.Yes:
            sys.exit()
        elif mbox==QMessageBox.No:
            print("you entered no")


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()
