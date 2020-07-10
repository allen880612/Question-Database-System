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
        MainWindow.resize(808, 296)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_add_unit = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(18)
        self.label_add_unit.setFont(font)
        self.label_add_unit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_add_unit.setObjectName("label_add_unit")
        self.gridLayout.addWidget(self.label_add_unit, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_lv5 = QtWidgets.QLabel(self.centralwidget)
        self.label_lv5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lv5.setObjectName("label_lv5")
        self.gridLayout_2.addWidget(self.label_lv5, 0, 4, 1, 1)
        self.label_lv3 = QtWidgets.QLabel(self.centralwidget)
        self.label_lv3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lv3.setObjectName("label_lv3")
        self.gridLayout_2.addWidget(self.label_lv3, 0, 2, 1, 1)
        self.label_lv4 = QtWidgets.QLabel(self.centralwidget)
        self.label_lv4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lv4.setObjectName("label_lv4")
        self.gridLayout_2.addWidget(self.label_lv4, 0, 3, 1, 1)
        self.label_lv1 = QtWidgets.QLabel(self.centralwidget)
        self.label_lv1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lv1.setObjectName("label_lv1")
        self.gridLayout_2.addWidget(self.label_lv1, 0, 0, 1, 1)
        self.label_lv2 = QtWidgets.QLabel(self.centralwidget)
        self.label_lv2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lv2.setObjectName("label_lv2")
        self.gridLayout_2.addWidget(self.label_lv2, 0, 1, 1, 1)
        self.textBox_lv1 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox_lv1.setObjectName("textBox_lv1")
        self.gridLayout_2.addWidget(self.textBox_lv1, 1, 0, 1, 1)
        self.textBox_lv2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox_lv2.setObjectName("textBox_lv2")
        self.gridLayout_2.addWidget(self.textBox_lv2, 1, 1, 1, 1)
        self.textBox_lv3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox_lv3.setObjectName("textBox_lv3")
        self.gridLayout_2.addWidget(self.textBox_lv3, 1, 2, 1, 1)
        self.textBox_lv4 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox_lv4.setObjectName("textBox_lv4")
        self.gridLayout_2.addWidget(self.textBox_lv4, 1, 3, 1, 1)
        self.textBox_lv5 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox_lv5.setObjectName("textBox_lv5")
        self.gridLayout_2.addWidget(self.textBox_lv5, 1, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_add_unit_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_unit_confirm.setObjectName("button_add_unit_confirm")
        self.horizontalLayout_2.addWidget(self.button_add_unit_confirm)
        self.button_add_unit_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_unit_cancel.setObjectName("button_add_unit_cancel")
        self.horizontalLayout_2.addWidget(self.button_add_unit_cancel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
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
        self.label_add_unit.setText(_translate("MainWindow", "新增單元"))
        self.label_lv5.setText(_translate("MainWindow", "單元"))
        self.label_lv3.setText(_translate("MainWindow", "題型 - 二"))
        self.label_lv4.setText(_translate("MainWindow", "主題"))
        self.label_lv1.setText(_translate("MainWindow", "科目"))
        self.label_lv2.setText(_translate("MainWindow", "題型 - 一"))
        self.button_add_unit_confirm.setText(_translate("MainWindow", "確定新增"))
        self.button_add_unit_cancel.setText(_translate("MainWindow", "取消新增"))


