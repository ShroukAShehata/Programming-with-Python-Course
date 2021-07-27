import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
        label1 = QLabel("Name" , self)
        label1.move(50,50)
        label2 = QLabel("Mail" , self)
        label2.move(50,100)
        label3 = QLabel("Mobile" , self)
        label3.move(50,150)
        label4 = QLabel("Password" , self)
        label4.move(50,200)
        label5 = QLabel("Track" , self)
        label5.move(50,250)
        label6 = QLabel("Group",self)
        label6.move(50,300)




        nametext = QLineEdit(self)
        nametext.move(150,50)
        nametext.setPlaceholderText("Enter your name")

        mailtext = QLineEdit(self)
        mailtext.move(150,100)
        mailtext.setPlaceholderText("Enter your email")

        mobiletext = QLineEdit(self)
        mobiletext.move(150,150)
        mobiletext.setPlaceholderText("Enter your mobile")

        passwordtext = QLineEdit(self)
        passwordtext.move(150,200)
        passwordtext.setEchoMode(QLineEdit.Password)

        tracks = QComboBox(self)
        tracks.move(150,250)
        tracks.addItems(["Python","Web Design","Networks"])

        malegender = QRadioButton("male",self )
        malegender.move(60 , 350)
        femalegender = QRadioButton("female",self)
        femalegender.move(130,350)

        group = QSpinBox(self)
        group.move(150,300)
        group.setRange(1,5)
        group.setSuffix(" group")





























app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()








