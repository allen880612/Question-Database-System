# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Unit_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class AddUnitPage_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 211)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBox_lv2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox_lv2.setObjectName("textBox_lv2")
        self.gridLayout_3.addWidget(self.textBox_lv2, 2, 1, 1, 1)
        self.label_lv1 = QtWidgets.QLabel(self.centralwidget)
        self.label_lv1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lv1.setObjectName("label_lv1")
        self.gridLayout_3.addWidget(self.label_lv1, 0, 0, 1, 1)
        self.textBox_lv1 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox_lv1.setObjectName("textBox_lv1")
        self.gridLayout_3.addWidget(self.textBox_lv1, 2, 0, 1, 1)
        self.label_lv2 = QtWidgets.QLabel(self.centralwidget)
        self.label_lv2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lv2.setObjectName("label_lv2")
        self.gridLayout_3.addWidget(self.label_lv2, 0, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.button_delete_level = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete_level.setObjectName("button_delete_level")
        self.verticalLayout_3.addWidget(self.button_delete_level)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.button_add_level = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_level.setObjectName("button_add_level")
        self.verticalLayout_3.addWidget(self.button_add_level)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.label_add_unit = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(18)
        self.label_add_unit.setFont(font)
        self.label_add_unit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_add_unit.setObjectName("label_add_unit")
        self.gridLayout.addWidget(self.label_add_unit, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_add_unit_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_unit_confirm.setObjectName("button_add_unit_confirm")
        self.horizontalLayout_2.addWidget(self.button_add_unit_confirm)
        self.button_add_unit_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_unit_cancel.setObjectName("button_add_unit_cancel")
        self.horizontalLayout_2.addWidget(self.button_add_unit_cancel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
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
        self.label_lv1.setText(_translate("MainWindow", "科目"))
        self.label_lv2.setText(_translate("MainWindow", "單元"))
        self.button_delete_level.setText(_translate("MainWindow", "－"))
        self.button_add_level.setText(_translate("MainWindow", "＋"))
        self.label_add_unit.setText(_translate("MainWindow", "新增單元"))
        self.button_add_unit_confirm.setText(_translate("MainWindow", "確定新增"))
        self.button_add_unit_cancel.setText(_translate("MainWindow", "取消新增"))


