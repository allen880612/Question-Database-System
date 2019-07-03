# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QDS\view\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 571, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setGeometry(QtCore.QRect(160, 300, 75, 23))
        self.btn_confirm.setObjectName("btn_confirm")
        self.cBox_dir1 = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_dir1.setGeometry(QtCore.QRect(60, 200, 121, 21))
        self.cBox_dir1.setObjectName("cBox_dir1")
        self.cBox_dir2 = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_dir2.setGeometry(QtCore.QRect(210, 200, 121, 21))
        self.cBox_dir2.setObjectName("cBox_dir2")
        self.cBox_word = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_word.setGeometry(QtCore.QRect(360, 200, 191, 21))
        self.cBox_word.setObjectName("cBox_word")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 180, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 180, 71, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Question Database"))
        self.label.setText(_translate("MainWindow", "請選擇試題範圍"))
        self.btn_confirm.setText(_translate("MainWindow", "確定"))
        self.label_2.setText(_translate("MainWindow", "資料夾 一層"))
        self.label_3.setText(_translate("MainWindow", "資料夾 二層"))
        self.label_4.setText(_translate("MainWindow", "Word"))

