# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Edit_Question_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class AddEditQuestionPage_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.text_edit_question = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_edit_question.setObjectName("text_edit_question")
        self.verticalLayout_5.addWidget(self.text_edit_question)
        self.gridLayout.addLayout(self.verticalLayout_5, 7, 1, 1, 1)
        self.label_question_level = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_question_level.setFont(font)
        self.label_question_level.setAlignment(QtCore.Qt.AlignCenter)
        self.label_question_level.setObjectName("label_question_level")
        self.gridLayout.addWidget(self.label_question_level, 3, 1, 1, 1)
        self.label_add_edit_question = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(18)
        self.label_add_edit_question.setFont(font)
        self.label_add_edit_question.setAlignment(QtCore.Qt.AlignCenter)
        self.label_add_edit_question.setObjectName("label_add_edit_question")
        self.gridLayout.addWidget(self.label_add_edit_question, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.button_solution = QtWidgets.QPushButton(self.centralwidget)
        self.button_solution.setObjectName("button_solution")
        self.horizontalLayout_4.addWidget(self.button_solution)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_add_question_mode = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_question_mode.setObjectName("button_add_question_mode")
        self.horizontalLayout_2.addWidget(self.button_add_question_mode)
        self.button_edit_question_mode = QtWidgets.QPushButton(self.centralwidget)
        self.button_edit_question_mode.setObjectName("button_edit_question_mode")
        self.horizontalLayout_2.addWidget(self.button_edit_question_mode)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_question_list = QtWidgets.QLabel(self.centralwidget)
        self.label_question_list.setAlignment(QtCore.Qt.AlignCenter)
        self.label_question_list.setObjectName("label_question_list")
        self.verticalLayout_4.addWidget(self.label_question_list)
        self.list_weight_question = QtWidgets.QListWidget(self.centralwidget)
        self.list_weight_question.setObjectName("list_weight_question")
        self.verticalLayout_4.addWidget(self.list_weight_question)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.list_widget_option = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_option.setObjectName("list_widget_option")
        self.verticalLayout_4.addWidget(self.list_widget_option)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_add_option = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_option.setObjectName("button_add_option")
        self.horizontalLayout_5.addWidget(self.button_add_option)
        self.button_remove_option = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove_option.setObjectName("button_remove_option")
        self.horizontalLayout_5.addWidget(self.button_remove_option)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_4, 7, 0, 1, 1)
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        self.button_return.setObjectName("button_return")
        self.gridLayout.addWidget(self.button_return, 8, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_image_preview_text = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image_preview_text.sizePolicy().hasHeightForWidth())
        self.label_image_preview_text.setSizePolicy(sizePolicy)
        self.label_image_preview_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_preview_text.setObjectName("label_image_preview_text")
        self.gridLayout_3.addWidget(self.label_image_preview_text, 6, 0, 1, 1)
        self.label_image_list = QtWidgets.QLabel(self.centralwidget)
        self.label_image_list.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_list.setObjectName("label_image_list")
        self.gridLayout_3.addWidget(self.label_image_list, 0, 0, 1, 1)
        self.label_image_preview = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image_preview.sizePolicy().hasHeightForWidth())
        self.label_image_preview.setSizePolicy(sizePolicy)
        self.label_image_preview.setScaledContents(False)
        self.label_image_preview.setObjectName("label_image_preview")
        self.gridLayout_3.addWidget(self.label_image_preview, 7, 0, 1, 1)
        self.verticalLayout_questionList = QtWidgets.QVBoxLayout()
        self.verticalLayout_questionList.setObjectName("verticalLayout_questionList")
        self.button_import_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_import_image.setObjectName("button_import_image")
        self.verticalLayout_questionList.addWidget(self.button_import_image)
        self.button_addToList_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_addToList_image.setObjectName("button_addToList_image")
        self.verticalLayout_questionList.addWidget(self.button_addToList_image)
        self.button_delete_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete_image.setObjectName("button_delete_image")
        self.verticalLayout_questionList.addWidget(self.button_delete_image)
        self.gridLayout_3.addLayout(self.verticalLayout_questionList, 4, 1, 1, 1)
        self.list_weight_image = QtWidgets.QListWidget(self.centralwidget)
        self.list_weight_image.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_weight_image.sizePolicy().hasHeightForWidth())
        self.list_weight_image.setSizePolicy(sizePolicy)
        self.list_weight_image.setObjectName("list_weight_image")
        self.gridLayout_3.addWidget(self.list_weight_image, 4, 0, 1, 1)
        self.button_add_question = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add_question.sizePolicy().hasHeightForWidth())
        self.button_add_question.setSizePolicy(sizePolicy)
        self.button_add_question.setMaximumSize(QtCore.QSize(100, 40))
        self.button_add_question.setObjectName("button_add_question")
        self.gridLayout_3.addWidget(self.button_add_question, 7, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 7, 3, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_FillingQuestion = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_FillingQuestion.setObjectName("radioButton_FillingQuestion")
        self.horizontalLayout_3.addWidget(self.radioButton_FillingQuestion)
        self.radioButton_SelectQuestion = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_SelectQuestion.setObjectName("radioButton_SelectQuestion")
        self.horizontalLayout_3.addWidget(self.radioButton_SelectQuestion)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
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
        self.label_3.setText(_translate("MainWindow", "題目內容"))
        self.label_question_level.setText(_translate("MainWindow", "TextLabel"))
        self.label_add_edit_question.setText(_translate("MainWindow", "新增題目"))
        self.button_solution.setText(_translate("MainWindow", "詳解"))
        self.button_add_question_mode.setText(_translate("MainWindow", "新增題目"))
        self.button_edit_question_mode.setText(_translate("MainWindow", "修改題目"))
        self.label_question_list.setText(_translate("MainWindow", "題目列表"))
        self.label.setText(_translate("MainWindow", "選項列表"))
        self.button_add_option.setText(_translate("MainWindow", "新增選項"))
        self.button_remove_option.setText(_translate("MainWindow", "移除選項"))
        self.button_return.setText(_translate("MainWindow", "返回"))
        self.label_image_preview_text.setText(_translate("MainWindow", "圖片預覽"))
        self.label_image_list.setText(_translate("MainWindow", "圖片列表"))
        self.label_image_preview.setText(_translate("MainWindow", "TextLabel"))
        self.button_import_image.setText(_translate("MainWindow", "匯入圖片"))
        self.button_addToList_image.setText(_translate("MainWindow", "新增至列表"))
        self.button_delete_image.setText(_translate("MainWindow", "刪除圖片"))
        self.button_add_question.setText(_translate("MainWindow", "新增題目"))
        self.radioButton_FillingQuestion.setText(_translate("MainWindow", "填充題"))
        self.radioButton_SelectQuestion.setText(_translate("MainWindow", "選擇題"))


