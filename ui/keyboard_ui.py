# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyboard-ui.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 468)
        MainWindow.setStyleSheet("#MainWindow {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,     stop:0 rgba(20, 20, 20, 255), stop:1 rgba(40, 40, 40, 1));\n"
"}\n"
"\n"
"#key_space { \n"
"    min-width: 580;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0C7D16, stop:1 #21CF30);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0C7D16, stop:1 #009E0D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0C7D16, stop:1 #31DF40);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0C7D16, stop:1 #009E0D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_computer = QtWidgets.QLabel(self.centralwidget)
        self.label_computer.setText("")
        self.label_computer.setObjectName("label_computer")
        self.verticalLayout_3.addWidget(self.label_computer)
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setText("")
        self.label_user.setObjectName("label_user")
        self.verticalLayout_3.addWidget(self.label_user)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.key_caps = QtWidgets.QPushButton(self.centralwidget)
        self.key_caps.setStyleSheet("#key_caps {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3252B2, stop:1 #4775FF);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_caps:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_caps:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"}\n"
"\n"
"#key_caps:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_caps.setObjectName("key_caps")
        self.horizontalLayout_3.addWidget(self.key_caps)
        self.key_a = QtWidgets.QPushButton(self.centralwidget)
        self.key_a.setObjectName("key_a")
        self.horizontalLayout_3.addWidget(self.key_a)
        self.key_s = QtWidgets.QPushButton(self.centralwidget)
        self.key_s.setStyleSheet("#key_s {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #008A8A, stop:1 #33A1A1);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_s:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_s:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"}\n"
"\n"
"#key_s:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_s.setObjectName("key_s")
        self.horizontalLayout_3.addWidget(self.key_s)
        self.key_d = QtWidgets.QPushButton(self.centralwidget)
        self.key_d.setStyleSheet("#key_d {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E64848, stop:1 #EB6D6D);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_d:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_d:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"}\n"
"\n"
"#key_d:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_d.setObjectName("key_d")
        self.horizontalLayout_3.addWidget(self.key_d)
        self.key_f = QtWidgets.QPushButton(self.centralwidget)
        self.key_f.setStyleSheet("#key_f {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF9900, stop:1 #FFAD33);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_f:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_f:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"}\n"
"\n"
"#key_f:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_f.setObjectName("key_f")
        self.horizontalLayout_3.addWidget(self.key_f)
        self.key_g = QtWidgets.QPushButton(self.centralwidget)
        self.key_g.setStyleSheet("#key_g {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF9900, stop:1 #FFAD33);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_g:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_g:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"}\n"
"\n"
"#key_g:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_g.setObjectName("key_g")
        self.horizontalLayout_3.addWidget(self.key_g)
        self.key_h = QtWidgets.QPushButton(self.centralwidget)
        self.key_h.setStyleSheet("#key_h {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #660066, stop:1 #853385);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_h:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_h:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"}\n"
"\n"
"#key_h:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_h.setObjectName("key_h")
        self.horizontalLayout_3.addWidget(self.key_h)
        self.key_j = QtWidgets.QPushButton(self.centralwidget)
        self.key_j.setStyleSheet("#key_j {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #660066, stop:1 #853385);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_j:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_j:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"}\n"
"\n"
"#key_j:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_j.setObjectName("key_j")
        self.horizontalLayout_3.addWidget(self.key_j)
        self.key_k = QtWidgets.QPushButton(self.centralwidget)
        self.key_k.setStyleSheet("#key_k {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E64848, stop:1 #EB6D6D);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_k:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_k:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"}\n"
"\n"
"#key_k:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_k.setObjectName("key_k")
        self.horizontalLayout_3.addWidget(self.key_k)
        self.key_l = QtWidgets.QPushButton(self.centralwidget)
        self.key_l.setStyleSheet("#key_l {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #008A8A, stop:1 #33A1A1);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_l:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_l:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"}\n"
"\n"
"#key_l:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_l.setObjectName("key_l")
        self.horizontalLayout_3.addWidget(self.key_l)
        self.key_semicolon = QtWidgets.QPushButton(self.centralwidget)
        self.key_semicolon.setObjectName("key_semicolon")
        self.horizontalLayout_3.addWidget(self.key_semicolon)
        self.key_apostrophe = QtWidgets.QPushButton(self.centralwidget)
        self.key_apostrophe.setObjectName("key_apostrophe")
        self.horizontalLayout_3.addWidget(self.key_apostrophe)
        self.key_enter = QtWidgets.QPushButton(self.centralwidget)
        self.key_enter.setStyleSheet("#key_enter {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3252B2, stop:1 #4775FF);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_enter:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_enter:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"}\n"
"\n"
"#key_enter:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_enter.setObjectName("key_enter")
        self.horizontalLayout_3.addWidget(self.key_enter)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.key_tilde = QtWidgets.QPushButton(self.centralwidget)
        self.key_tilde.setStyleSheet("#key_tilde {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3252B2, stop:1 #4775FF);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_tilde:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_tilde:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"}\n"
"\n"
"#key_tilde:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_tilde.setObjectName("key_tilde")
        self.horizontalLayout.addWidget(self.key_tilde)
        self.key_1 = QtWidgets.QPushButton(self.centralwidget)
        self.key_1.setObjectName("key_1")
        self.horizontalLayout.addWidget(self.key_1)
        self.key_2 = QtWidgets.QPushButton(self.centralwidget)
        self.key_2.setStyleSheet("#key_2 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #008A8A, stop:1 #33A1A1);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_2:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_2:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"}\n"
"\n"
"#key_2:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_2.setObjectName("key_2")
        self.horizontalLayout.addWidget(self.key_2)
        self.key_3 = QtWidgets.QPushButton(self.centralwidget)
        self.key_3.setStyleSheet("#key_3 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E64848, stop:1 #EB6D6D);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_3:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_3:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"}\n"
"\n"
"#key_3:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_3.setObjectName("key_3")
        self.horizontalLayout.addWidget(self.key_3)
        self.key_4 = QtWidgets.QPushButton(self.centralwidget)
        self.key_4.setStyleSheet("#key_4 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF9900, stop:1 #FFAD33);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_4:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_4:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"}\n"
"\n"
"#key_4:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_4.setObjectName("key_4")
        self.horizontalLayout.addWidget(self.key_4)
        self.key_5 = QtWidgets.QPushButton(self.centralwidget)
        self.key_5.setStyleSheet("#key_5 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF9900, stop:1 #FFAD33);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_5:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_5:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"}\n"
"\n"
"#key_5:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_5.setObjectName("key_5")
        self.horizontalLayout.addWidget(self.key_5)
        self.key_6 = QtWidgets.QPushButton(self.centralwidget)
        self.key_6.setStyleSheet("#key_6 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #660066, stop:1 #853385);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_6:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_6:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"}\n"
"\n"
"#key_6:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_6.setObjectName("key_6")
        self.horizontalLayout.addWidget(self.key_6)
        self.key_7 = QtWidgets.QPushButton(self.centralwidget)
        self.key_7.setStyleSheet("#key_7 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #660066, stop:1 #853385);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_7:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_7:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"}\n"
"\n"
"#key_7:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_7.setObjectName("key_7")
        self.horizontalLayout.addWidget(self.key_7)
        self.key_8 = QtWidgets.QPushButton(self.centralwidget)
        self.key_8.setStyleSheet("#key_8 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E64848, stop:1 #EB6D6D);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_8:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_8:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"}\n"
"\n"
"#key_8:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_8.setObjectName("key_8")
        self.horizontalLayout.addWidget(self.key_8)
        self.key_9 = QtWidgets.QPushButton(self.centralwidget)
        self.key_9.setStyleSheet("#key_9 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #008A8A, stop:1 #33A1A1);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_9:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_9:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"}\n"
"\n"
"#key_9:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_9.setObjectName("key_9")
        self.horizontalLayout.addWidget(self.key_9)
        self.key_0 = QtWidgets.QPushButton(self.centralwidget)
        self.key_0.setObjectName("key_0")
        self.horizontalLayout.addWidget(self.key_0)
        self.key_dash = QtWidgets.QPushButton(self.centralwidget)
        self.key_dash.setObjectName("key_dash")
        self.horizontalLayout.addWidget(self.key_dash)
        self.key_equals = QtWidgets.QPushButton(self.centralwidget)
        self.key_equals.setObjectName("key_equals")
        self.horizontalLayout.addWidget(self.key_equals)
        self.key_back = QtWidgets.QPushButton(self.centralwidget)
        self.key_back.setStyleSheet("#key_back {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3252B2, stop:1 #4775FF);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_back:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_back:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"}\n"
"\n"
"#key_back:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_back.setObjectName("key_back")
        self.horizontalLayout.addWidget(self.key_back)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.key_tab = QtWidgets.QPushButton(self.centralwidget)
        self.key_tab.setStyleSheet("#key_tab {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3252B2, stop:1 #4775FF);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_tab:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_tab:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"}\n"
"\n"
"#key_tab:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_tab.setObjectName("key_tab")
        self.horizontalLayout_2.addWidget(self.key_tab)
        self.key_q = QtWidgets.QPushButton(self.centralwidget)
        self.key_q.setObjectName("key_q")
        self.horizontalLayout_2.addWidget(self.key_q)
        self.key_w = QtWidgets.QPushButton(self.centralwidget)
        self.key_w.setStyleSheet("#key_w {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #008A8A, stop:1 #33A1A1);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_w:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_w:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"}\n"
"\n"
"#key_w:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_w.setObjectName("key_w")
        self.horizontalLayout_2.addWidget(self.key_w)
        self.key_e = QtWidgets.QPushButton(self.centralwidget)
        self.key_e.setStyleSheet("#key_e {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E64848, stop:1 #EB6D6D);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_e:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_e:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"}\n"
"\n"
"#key_e:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_e.setObjectName("key_e")
        self.horizontalLayout_2.addWidget(self.key_e)
        self.key_r = QtWidgets.QPushButton(self.centralwidget)
        self.key_r.setStyleSheet("#key_r {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF9900, stop:1 #FFAD33);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_r:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_r:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"}\n"
"\n"
"#key_r:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_r.setObjectName("key_r")
        self.horizontalLayout_2.addWidget(self.key_r)
        self.key_t = QtWidgets.QPushButton(self.centralwidget)
        self.key_t.setStyleSheet("#key_t {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF9900, stop:1 #FFAD33);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_t:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_t:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"}\n"
"\n"
"#key_t:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_t.setObjectName("key_t")
        self.horizontalLayout_2.addWidget(self.key_t)
        self.key_y = QtWidgets.QPushButton(self.centralwidget)
        self.key_y.setStyleSheet("#key_y {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #660066, stop:1 #853385);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_y:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_y:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"}\n"
"\n"
"#key_y:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_y.setObjectName("key_y")
        self.horizontalLayout_2.addWidget(self.key_y)
        self.key_u = QtWidgets.QPushButton(self.centralwidget)
        self.key_u.setStyleSheet("#key_u {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #660066, stop:1 #853385);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_u:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_u:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"}\n"
"\n"
"#key_u:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_u.setObjectName("key_u")
        self.horizontalLayout_2.addWidget(self.key_u)
        self.key_i = QtWidgets.QPushButton(self.centralwidget)
        self.key_i.setStyleSheet("#key_i {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E64848, stop:1 #EB6D6D);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_i:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_i:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"}\n"
"\n"
"#key_i:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_i.setObjectName("key_i")
        self.horizontalLayout_2.addWidget(self.key_i)
        self.key_o = QtWidgets.QPushButton(self.centralwidget)
        self.key_o.setStyleSheet("#key_o {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #008A8A, stop:1 #33A1A1);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_o:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_o:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"}\n"
"\n"
"#key_o:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_o.setObjectName("key_o")
        self.horizontalLayout_2.addWidget(self.key_o)
        self.key_p = QtWidgets.QPushButton(self.centralwidget)
        self.key_p.setObjectName("key_p")
        self.horizontalLayout_2.addWidget(self.key_p)
        self.key_sqrbrkt_left = QtWidgets.QPushButton(self.centralwidget)
        self.key_sqrbrkt_left.setObjectName("key_sqrbrkt_left")
        self.horizontalLayout_2.addWidget(self.key_sqrbrkt_left)
        self.key_sqrbrkt_right = QtWidgets.QPushButton(self.centralwidget)
        self.key_sqrbrkt_right.setObjectName("key_sqrbrkt_right")
        self.horizontalLayout_2.addWidget(self.key_sqrbrkt_right)
        self.key_back_slash = QtWidgets.QPushButton(self.centralwidget)
        self.key_back_slash.setStyleSheet("#key_back_slash {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3252B2, stop:1 #4775FF);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_back_slash:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_back_slash:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"}\n"
"\n"
"#key_back_slash:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_back_slash.setObjectName("key_back_slash")
        self.horizontalLayout_2.addWidget(self.key_back_slash)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.key_shift_left = QtWidgets.QPushButton(self.centralwidget)
        self.key_shift_left.setStyleSheet("#key_shift_left {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3252B2, stop:1 #4775FF);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_shift_left:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_shift_left:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"}\n"
"\n"
"#key_shift_left:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_shift_left.setObjectName("key_shift_left")
        self.horizontalLayout_4.addWidget(self.key_shift_left)
        self.key_z = QtWidgets.QPushButton(self.centralwidget)
        self.key_z.setObjectName("key_z")
        self.horizontalLayout_4.addWidget(self.key_z)
        self.key_x = QtWidgets.QPushButton(self.centralwidget)
        self.key_x.setStyleSheet("#key_x {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #008A8A, stop:1 #33A1A1);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_x:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_x:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"}\n"
"\n"
"#key_x:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_x.setObjectName("key_x")
        self.horizontalLayout_4.addWidget(self.key_x)
        self.key_c = QtWidgets.QPushButton(self.centralwidget)
        self.key_c.setStyleSheet("#key_c {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E64848, stop:1 #EB6D6D);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_c:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_c:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"}\n"
"\n"
"#key_c:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_c.setObjectName("key_c")
        self.horizontalLayout_4.addWidget(self.key_c)
        self.key_v = QtWidgets.QPushButton(self.centralwidget)
        self.key_v.setStyleSheet("#key_v {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF9900, stop:1 #FFAD33);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_v:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_v:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"}\n"
"\n"
"#key_v:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_v.setObjectName("key_v")
        self.horizontalLayout_4.addWidget(self.key_v)
        self.key_b = QtWidgets.QPushButton(self.centralwidget)
        self.key_b.setStyleSheet("#key_b {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF9900, stop:1 #FFAD33);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_b:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_b:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"}\n"
"\n"
"#key_b:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB547, stop:1 #FFAD33);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_b.setObjectName("key_b")
        self.horizontalLayout_4.addWidget(self.key_b)
        self.key_n = QtWidgets.QPushButton(self.centralwidget)
        self.key_n.setStyleSheet("#key_n {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #660066, stop:1 #853385);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_n:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_n:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"}\n"
"\n"
"#key_n:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_n.setObjectName("key_n")
        self.horizontalLayout_4.addWidget(self.key_n)
        self.key_m = QtWidgets.QPushButton(self.centralwidget)
        self.key_m.setStyleSheet("#key_m {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #660066, stop:1 #853385);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_m:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_m:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"}\n"
"\n"
"#key_m:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #782E78, stop:1 #853385);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_m.setObjectName("key_m")
        self.horizontalLayout_4.addWidget(self.key_m)
        self.key_comma = QtWidgets.QPushButton(self.centralwidget)
        self.key_comma.setStyleSheet("#key_comma {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E64848, stop:1 #EB6D6D);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_comma:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_comma:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"}\n"
"\n"
"#key_comma:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ED7C7C, stop:1 #EB6D6D);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_comma.setObjectName("key_comma")
        self.horizontalLayout_4.addWidget(self.key_comma)
        self.key_dot = QtWidgets.QPushButton(self.centralwidget)
        self.key_dot.setStyleSheet("#key_dot {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #008A8A, stop:1 #33A1A1);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_dot:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_dot:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"}\n"
"\n"
"#key_dot:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #33A1A1, stop:1 #33A1A1);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_dot.setObjectName("key_dot")
        self.horizontalLayout_4.addWidget(self.key_dot)
        self.key_forward_slash = QtWidgets.QPushButton(self.centralwidget)
        self.key_forward_slash.setObjectName("key_forward_slash")
        self.horizontalLayout_4.addWidget(self.key_forward_slash)
        self.key_shift_right = QtWidgets.QPushButton(self.centralwidget)
        self.key_shift_right.setStyleSheet("#key_shift_right {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3252B2, stop:1 #4775FF);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 70;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_shift_right:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_shift_right:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"}\n"
"\n"
"#key_shift_right:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_shift_right.setObjectName("key_shift_right")
        self.horizontalLayout_4.addWidget(self.key_shift_right)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.key_space = QtWidgets.QPushButton(self.centralwidget)
        self.key_space.setStyleSheet("#key_space {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3252B2, stop:1 #4775FF);\n"
"    border: 1px solid gray;\n"
"    font: 20px;\n"
"    padding: 6px;\n"
"    min-width: 580;\n"
"    min-height: 70;\n"
"    max-width: 200;\n"
"    max-height: 200;\n"
"}\n"
"\n"
"#key_space:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}\n"
"\n"
"#key_space:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"}\n"
"\n"
"#key_space:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4663BA, stop:1 #4775FF);\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: red;\n"
"}")
        self.key_space.setObjectName("key_space")
        self.horizontalLayout_5.addWidget(self.key_space)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Computer: "))
        self.label_2.setText(_translate("MainWindow", "User       : "))
        self.key_caps.setText(_translate("MainWindow", "CAPS"))
        self.key_a.setText(_translate("MainWindow", "a"))
        self.key_s.setText(_translate("MainWindow", "s"))
        self.key_d.setText(_translate("MainWindow", "d"))
        self.key_f.setText(_translate("MainWindow", "f"))
        self.key_g.setText(_translate("MainWindow", "g"))
        self.key_h.setText(_translate("MainWindow", "h"))
        self.key_j.setText(_translate("MainWindow", "j"))
        self.key_k.setText(_translate("MainWindow", "k"))
        self.key_l.setText(_translate("MainWindow", "l"))
        self.key_semicolon.setText(_translate("MainWindow", ";"))
        self.key_apostrophe.setText(_translate("MainWindow", "\'"))
        self.key_enter.setText(_translate("MainWindow", "ENTER"))
        self.key_tilde.setText(_translate("MainWindow", "`"))
        self.key_1.setText(_translate("MainWindow", "1"))
        self.key_2.setText(_translate("MainWindow", "2"))
        self.key_3.setText(_translate("MainWindow", "3"))
        self.key_4.setText(_translate("MainWindow", "4"))
        self.key_5.setText(_translate("MainWindow", "5"))
        self.key_6.setText(_translate("MainWindow", "6"))
        self.key_7.setText(_translate("MainWindow", "7"))
        self.key_8.setText(_translate("MainWindow", "8"))
        self.key_9.setText(_translate("MainWindow", "9"))
        self.key_0.setText(_translate("MainWindow", "0"))
        self.key_dash.setText(_translate("MainWindow", "-"))
        self.key_equals.setText(_translate("MainWindow", "="))
        self.key_back.setText(_translate("MainWindow", "Back"))
        self.key_tab.setText(_translate("MainWindow", "TAB"))
        self.key_q.setText(_translate("MainWindow", "q"))
        self.key_w.setText(_translate("MainWindow", "w"))
        self.key_e.setText(_translate("MainWindow", "e"))
        self.key_r.setText(_translate("MainWindow", "r"))
        self.key_t.setText(_translate("MainWindow", "t"))
        self.key_y.setText(_translate("MainWindow", "y"))
        self.key_u.setText(_translate("MainWindow", "u"))
        self.key_i.setText(_translate("MainWindow", "i"))
        self.key_o.setText(_translate("MainWindow", "o"))
        self.key_p.setText(_translate("MainWindow", "p"))
        self.key_sqrbrkt_left.setText(_translate("MainWindow", "["))
        self.key_sqrbrkt_right.setText(_translate("MainWindow", "]"))
        self.key_back_slash.setText(_translate("MainWindow", "\\"))
        self.key_shift_left.setText(_translate("MainWindow", "SHIFT"))
        self.key_z.setText(_translate("MainWindow", "z"))
        self.key_x.setText(_translate("MainWindow", "x"))
        self.key_c.setText(_translate("MainWindow", "c"))
        self.key_v.setText(_translate("MainWindow", "v"))
        self.key_b.setText(_translate("MainWindow", "b"))
        self.key_n.setText(_translate("MainWindow", "n"))
        self.key_m.setText(_translate("MainWindow", "m"))
        self.key_comma.setText(_translate("MainWindow", ","))
        self.key_dot.setText(_translate("MainWindow", "."))
        self.key_forward_slash.setText(_translate("MainWindow", "/"))
        self.key_shift_right.setText(_translate("MainWindow", "SHIFT"))
        self.key_space.setText(_translate("MainWindow", "SPACE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

