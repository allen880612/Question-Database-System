# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Select_Subject_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class SelectSubject_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.button_return.setFont(font)
        self.button_return.setObjectName("button_return")
        self.horizontalLayout_2.addWidget(self.button_return)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.button_confirm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.button_confirm.setFont(font)
        self.button_confirm.setObjectName("button_confirm")
        self.horizontalLayout_2.addWidget(self.button_confirm)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.label_select_subject = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_select_subject.setFont(font)
        self.label_select_subject.setAlignment(QtCore.Qt.AlignCenter)
        self.label_select_subject.setObjectName("label_select_subject")
        self.gridLayout.addWidget(self.label_select_subject, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_return.setText(_translate("MainWindow", "返回"))
        self.button_confirm.setText(_translate("MainWindow", "確定"))
        self.label_select_subject.setText(_translate("MainWindow", "選擇科目"))


