from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtWidgets, QtGui
from view.UI import Revise_MakeQuestion_UI 
from view import ComboboxView as cbview
from model import MyLibrary
import random
import os
import docx

class ReviseMakeQuestionPage(QMainWindow):

    revise_make_question_signal = QtCore.pyqtSignal(bool) # set 信號

    def __init__(self, _model):
        super(ReviseMakeQuestionPage, self).__init__()
        self.ui = Revise_MakeQuestion_UI.ReviseMakeQuestion_UI()
        self.ui.setupUi(self)
        self.model = _model
        self.is_click_button = False # 是否透過button關閉視窗
        self.listView = self.ui.listView_make_question_level
        self.tester = ["str1", "str2", "str8"]
        self.Initialize()

    # 初始化
    def Initialize(self):
        self.ConnectEvent()
        self.ResetPage()

    # 重設頁面
    def ResetPage(self):
        self.is_click_button = False
        

    # 註冊事件
    def ConnectEvent(self):
        self.ui.button_return.clicked.connect(self.ClosePage)

    # 關閉這個視窗
    def ClosePage(self):
        self.is_click_button = True
        is_close = self.close()
        self.revise_make_question_signal.emit(is_close)

    # 關閉視窗事件
    def closeEventI(self, event):
        if self.is_click_button == False:
            is_close = True
            self.revise_make_question_signal.emit(is_close)