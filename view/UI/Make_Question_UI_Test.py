# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'make_question_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class MakeQuestionPage_UI(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.cBoxList = [QtWidgets.QComboBox(self.centralwidget) for _ in range(5)]
        for i in range(5):
            self.CreateComboBox(i)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 70, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setGeometry(QtCore.QRect(624, 300, 121, 31))
        self.btn_confirm.setObjectName("btn_confirm")

        self.label_level2 = QtWidgets.QLabel(self.centralwidget)
        self.label_level2.setGeometry(QtCore.QRect(200, 175, 121, 21))
        self.label_level2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_level2.setObjectName("label_level2")

        self.label_level3 = QtWidgets.QLabel(self.centralwidget)
        self.label_level3.setGeometry(QtCore.QRect(340, 175, 121, 21))
        self.label_level3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_level3.setObjectName("label_level3")

        self.label_level4 = QtWidgets.QLabel(self.centralwidget)
        self.label_level4.setGeometry(QtCore.QRect(480, 175, 121, 21))
        self.label_level4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_level4.setObjectName("label_level4")

        self.label_level5 = QtWidgets.QLabel(self.centralwidget)
        self.label_level5.setGeometry(QtCore.QRect(620, 175, 121, 21))
        self.label_level5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_level5.setObjectName("label_level5")

        self.label_level1 = QtWidgets.QLabel(self.centralwidget)
        self.label_level1.setGeometry(QtCore.QRect(60, 170, 119, 23))
        self.label_level1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_level1.setObjectName("label_level1")

        MainWindow.setCentralWidget(self.centralwidget)
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
        self.label_level2.setText(_translate("MainWindow", "題型 - 一"))
        self.label_level3.setText(_translate("MainWindow", "題型 - 二"))
        self.label_level4.setText(_translate("MainWindow", "主題"))
        self.label_level5.setText(_translate("MainWindow", "單元"))
        self.label_level1.setText(_translate("MainWindow", "科目"))

    def CreateComboBox(self, i):

        self.cBoxList[i] = QtWidgets.QComboBox(self.centralwidget)
        self.cBoxList[i].setGeometry(QtCore.QRect(60 + i*140, 200, 120, 20))
        self.cBoxList[i].setObjectName("cBox_level" + str(i+1))


