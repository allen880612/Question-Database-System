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
        MainWindow.resize(628, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_0 = QtWidgets.QGridLayout()
        self.gridLayout_0.setObjectName("gridLayout_0")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_0.addItem(spacerItem, 0, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_return.sizePolicy().hasHeightForWidth())
        self.button_return.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.button_return.setFont(font)
        self.button_return.setObjectName("button_return")
        self.horizontalLayout_5.addWidget(self.button_return)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.button_make_question = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_make_question.sizePolicy().hasHeightForWidth())
        self.button_make_question.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.button_make_question.setFont(font)
        self.button_make_question.setObjectName("button_make_question")
        self.horizontalLayout_5.addWidget(self.button_make_question)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.gridLayout_0.addLayout(self.horizontalLayout_5, 7, 2, 1, 1)
        self.gridLayout_1 = QtWidgets.QGridLayout()
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.lineEdit_total_number = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.lineEdit_total_number.setFont(font)
        self.lineEdit_total_number.setObjectName("lineEdit_total_number")
        self.gridLayout_1.addWidget(self.lineEdit_total_number, 0, 3, 1, 1)
        self.label_total_number = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_total_number.setFont(font)
        self.label_total_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_number.setObjectName("label_total_number")
        self.gridLayout_1.addWidget(self.label_total_number, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1.addItem(spacerItem5, 0, 1, 1, 1)
        self.gridLayout_0.addLayout(self.gridLayout_1, 5, 2, 1, 1)
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
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
        self.gridLayout_0.addWidget(self.label_title, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_0.addItem(spacerItem6, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Question Database"))
        self.button_return.setText(_translate("MainWindow", "返回"))
        self.button_make_question.setText(_translate("MainWindow", "出題"))
        self.label_total_number.setText(_translate("MainWindow", "總題數"))
        self.label_title.setText(_translate("MainWindow", "選擇題數"))


