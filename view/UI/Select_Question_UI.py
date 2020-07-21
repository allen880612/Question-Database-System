# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Select_Question_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class SelectQuestion_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(1)
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.button_add_unit = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_unit.setObjectName("button_add_unit")
        self.horizontalLayout_7.addWidget(self.button_add_unit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.button_add_question = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_question.setObjectName("button_add_question")
        self.horizontalLayout_7.addWidget(self.button_add_question)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.button_make_question = QtWidgets.QPushButton(self.centralwidget)
        self.button_make_question.setObjectName("button_make_question")
        self.horizontalLayout_7.addWidget(self.button_make_question)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_add_edit_question = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(18)
        self.label_add_edit_question.setFont(font)
        self.label_add_edit_question.setAlignment(QtCore.Qt.AlignCenter)
        self.label_add_edit_question.setObjectName("label_add_edit_question")
        self.horizontalLayout_2.addWidget(self.label_add_edit_question)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_lv5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_lv5.setObjectName("verticalLayout_lv5")
        self.gridLayout.addLayout(self.verticalLayout_lv5, 3, 4, 1, 1)
        self.verticalLayout_lv1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_lv1.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_lv1.setSpacing(6)
        self.verticalLayout_lv1.setObjectName("verticalLayout_lv1")
        self.gridLayout.addLayout(self.verticalLayout_lv1, 3, 0, 1, 1)
        self.verticalLayout_lv4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_lv4.setObjectName("verticalLayout_lv4")
        self.gridLayout.addLayout(self.verticalLayout_lv4, 3, 3, 1, 1)
        self.verticalLayout_lv2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_lv2.setObjectName("verticalLayout_lv2")
        self.gridLayout.addLayout(self.verticalLayout_lv2, 3, 1, 1, 1)
        self.verticalLayout_lv3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_lv3.setObjectName("verticalLayout_lv3")
        self.gridLayout.addLayout(self.verticalLayout_lv3, 3, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_add_unit.setText(_translate("MainWindow", "新增單元"))
        self.button_add_question.setText(_translate("MainWindow", "新增題目"))
        self.button_make_question.setText(_translate("MainWindow", "出題"))
        self.label_add_edit_question.setText(_translate("MainWindow", "選擇題目階層"))