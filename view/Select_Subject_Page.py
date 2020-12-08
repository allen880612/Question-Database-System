from functools import partial
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QFrame, QSizePolicy
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtCore, QtWidgets
from model import MyLibrary
from model import QtExtend
from view.UI import Select_Subject_UI
from view import Add_Unit_Page
import pathlib
import os
import copy

class SelectSubjectPage(QMainWindow):
    
    #add_unit_signal = QtCore.pyqtSignal(bool, list) # set 信號

    def __init__(self, _model):
        super(SelectSubjectPage, self).__init__()

        self.ui = Select_Subject_UI.SelectSubject_UI()
        self.ui.setupUi(self)
        
        self.model = _model
        # 主layout
        self.main_layout = self.ui.gridLayout_2

        # 科目名稱list
        self.subject_list = []
        # 科目 button list
        self.subject_button_list = []
        # 目前選擇的科目
        self.current_button = None

        self.Initialize()

    # 初始化
    def Initialize(self):
        self.ConnectEvent()
        self.ResetPage()
        self.UpdateUI()

    # 註冊事件
    def ConnectEvent(self):
        return

    # ResetPage
    def ResetPage(self):
        self.subject_list = []
        self.subject_button_list = []
        self.current_button = None

        self.subject_list = self.model.GetSubjectNameList()

        #self.subject_list = ["數學", "理化", "國文", "社會"]
        self.ResetLayoutElement()

        self.UpdateUI()

    # 更新UI
    def UpdateUI(self):
        self.ui.button_confirm.setEnabled(self.current_button is not None)
        self.ui.button_return.setEnabled(False)

    # 重設Layout
    def ResetLayoutElement(self):
        k = 0
        for subject_name in self.subject_list:
            self.CreateSubjectLevel(subject_name, k)
            k += 1

    # 創造科目的Level
    def CreateSubjectLevel(self, subject_name, index):
        # Set Font
        font = QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setPointSize(18)

        # Set Button
        #subject_button = QtWidgets.Qbutton(self.ui.centralwidget)
        subject_button = QtWidgets.QPushButton(self.ui.centralwidget)
        subject_button.setFont(font)
        subject_button.setText(subject_name)
        subject_button.setObjectName(subject_name)
        subject_button.setFlat(True)
        subject_button.setStyleSheet(self.GetBlackBorderStyle())

        # Set Size Policy
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(subject_button.sizePolicy().hasHeightForWidth())
        subject_button.setSizePolicy(sizePolicy)

        subject_button.clicked.connect(self.ClickSubjectButton)
        self.main_layout.addWidget(subject_button, index // 2, index % 2, QtCore.Qt.AlignCenter)
        self.subject_button_list.append(subject_button)

    # Click Button
    def ClickSubjectButton(self):
        btn = self.sender()
        if self.current_button is not None:
            self.current_button.setStyleSheet(self.GetBlackBorderStyle())
        btn.setStyleSheet(self.GetRedBorderStyle())

        self.current_button = btn
        print(btn.text())

        self.UpdateUI()

    # 回傳 黑色邊框Style
    def GetBlackBorderStyle(self):
        style = 'border :2px solid ;border-color : black;'
        padding = 'padding-top: 25px;' + 'padding-bottom: 25px;' + 'padding-left: 50px;' + 'padding-right: 50px;'
        return style + padding

    # 回傳 紅色邊框Style
    def GetRedBorderStyle(self):
        style = 'border :2px solid ;border-color : red;'
        padding = 'padding-top: 25px;' + 'padding-bottom: 25px;' + 'padding-left: 50px;' + 'padding-right: 50px;'
        return style + padding

    # 得到選擇的科目
    def GetSelectSubject(self):
        subject = "Unknow"
        if self.current_button is not None:
            subject = self.current_button.text()
        return subject

    #def closeEvent(self, event):
    #    self.model.db.close()
