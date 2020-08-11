# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Revise_MakeQuestion_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class ReviseMakeQuestion_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 486)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        self.button_return.setObjectName("button_return")
        self.horizontalLayout_3.addWidget(self.button_return)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.button_continue = QtWidgets.QPushButton(self.centralwidget)
        self.button_continue.setObjectName("button_continue")
        self.horizontalLayout_3.addWidget(self.button_continue)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.listWidget_make_question_level = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_make_question_level.setObjectName("listWidget_make_question_level")
        self.horizontalLayout_6.addWidget(self.listWidget_make_question_level)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_none_select_question = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_none_select_question.setObjectName("listWidget_none_select_question")
        self.gridLayout_3.addWidget(self.listWidget_none_select_question, 1, 0, 1, 1)
        self.listWidget_selected_question = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_selected_question.setObjectName("listWidget_selected_question")
        self.gridLayout_3.addWidget(self.listWidget_selected_question, 1, 2, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.button_remove_question = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove_question.setObjectName("button_remove_question")
        self.horizontalLayout_8.addWidget(self.button_remove_question)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 0, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.button_add_question = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_question.setObjectName("button_add_question")
        self.horizontalLayout_7.addWidget(self.button_add_question)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_3)
        self.textEdit_preview_question = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_preview_question.setObjectName("textEdit_preview_question")
        self.horizontalLayout_6.addWidget(self.textEdit_preview_question)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
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
        self.button_continue.setText(_translate("MainWindow", "下一頁"))
        self.button_remove_question.setText(_translate("MainWindow", "←"))
        self.button_add_question.setText(_translate("MainWindow", "→"))


