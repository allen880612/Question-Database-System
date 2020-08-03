# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Make_Question_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class MakeQuestionPage_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_0 = QtWidgets.QGridLayout()
        self.gridLayout_0.setObjectName("gridLayout_0")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        self.button_return.setObjectName("button_return")
        self.horizontalLayout_5.addWidget(self.button_return)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.button_make_question = QtWidgets.QPushButton(self.centralwidget)
        self.button_make_question.setObjectName("button_make_question")
        self.horizontalLayout_5.addWidget(self.button_make_question)
        self.gridLayout_0.addLayout(self.horizontalLayout_5, 6, 2, 1, 1)
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_title.setFont(font)
        self.label_title.setTabletTracking(False)
        self.label_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title.setTextFormat(QtCore.Qt.RichText)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout_0.addWidget(self.label_title, 0, 2, 1, 1)
        self.gridLayout_1 = QtWidgets.QGridLayout()
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.lineEdit_total_number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_total_number.setObjectName("lineEdit_total_number")
        self.gridLayout_1.addWidget(self.lineEdit_total_number, 0, 3, 1, 1)
        self.label_total_number = QtWidgets.QLabel(self.centralwidget)
        self.label_total_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_number.setObjectName("label_total_number")
        self.gridLayout_1.addWidget(self.label_total_number, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem1, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_0.addLayout(self.gridLayout_1, 4, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Question Database"))
        self.button_return.setText(_translate("MainWindow", "返回"))
        self.button_make_question.setText(_translate("MainWindow", "出題"))
        self.label_title.setText(_translate("MainWindow", "選擇題數"))
        self.label_total_number.setText(_translate("MainWindow", "總題數"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


