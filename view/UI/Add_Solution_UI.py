# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Solution_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class AddSolutionPage_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 385)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_solution_title = QtWidgets.QLabel(self.centralwidget)
        self.label_solution_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_solution_title.setObjectName("label_solution_title")
        self.verticalLayout.addWidget(self.label_solution_title)
        self.textEdit_solution = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit_solution.setMinimumSize(QtCore.QSize(300, 0))
        self.textEdit_solution.setObjectName("textEdit_solution")
        self.verticalLayout.addWidget(self.textEdit_solution)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.button_back_page = QtWidgets.QPushButton(self.centralwidget)
        self.button_back_page.setObjectName("button_back_page")
        self.gridLayout.addWidget(self.button_back_page, 3, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_preview_image = QtWidgets.QLabel(self.centralwidget)
        self.label_preview_image.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_preview_image.sizePolicy().hasHeightForWidth())
        self.label_preview_image.setSizePolicy(sizePolicy)
        self.label_preview_image.setMinimumSize(QtCore.QSize(0, 0))
        self.label_preview_image.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_preview_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_preview_image.setObjectName("label_preview_image")
        self.gridLayout_2.addWidget(self.label_preview_image, 3, 0, 1, 1)
        self.label_image_list = QtWidgets.QLabel(self.centralwidget)
        self.label_image_list.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_list.setObjectName("label_image_list")
        self.gridLayout_2.addWidget(self.label_image_list, 0, 0, 1, 1)
        self.list_widget_image = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_widget_image.sizePolicy().hasHeightForWidth())
        self.list_widget_image.setSizePolicy(sizePolicy)
        self.list_widget_image.setObjectName("list_widget_image")
        self.gridLayout_2.addWidget(self.list_widget_image, 1, 0, 1, 1)
        self.label_image_preview_title = QtWidgets.QLabel(self.centralwidget)
        self.label_image_preview_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_preview_title.setObjectName("label_image_preview_title")
        self.gridLayout_2.addWidget(self.label_image_preview_title, 2, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_add_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_image.setObjectName("button_add_image")
        self.verticalLayout_3.addWidget(self.button_add_image)
        self.button_add_list = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_list.setObjectName("button_add_list")
        self.verticalLayout_3.addWidget(self.button_add_list)
        self.button_delete_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete_image.setObjectName("button_delete_image")
        self.verticalLayout_3.addWidget(self.button_delete_image)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.button_store = QtWidgets.QPushButton(self.centralwidget)
        self.button_store.setMinimumSize(QtCore.QSize(0, 64))
        self.button_store.setObjectName("button_store")
        self.gridLayout_2.addWidget(self.button_store, 2, 1, 3, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 3, 1, 1)
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
        self.label_solution_title.setText(_translate("MainWindow", "詳解內容"))
        self.button_back_page.setText(_translate("MainWindow", "返回"))
        self.label_preview_image.setText(_translate("MainWindow", "TextLabel"))
        self.label_image_list.setText(_translate("MainWindow", "圖片列表"))
        self.label_image_preview_title.setText(_translate("MainWindow", "圖片預覽"))
        self.button_add_image.setText(_translate("MainWindow", "匯入圖片"))
        self.button_add_list.setText(_translate("MainWindow", "新增至列表"))
        self.button_delete_image.setText(_translate("MainWindow", "刪除圖片"))
        self.button_store.setText(_translate("MainWindow", "儲存詳解"))