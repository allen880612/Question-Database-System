from functools import partial
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from model import MyLibrary
from view.UI import Add_Unit_UI
from view import ComboboxView as cbView
import pathlib
import os

class AddUnitPage(QMainWindow):
    
    add_unit_signal = QtCore.pyqtSignal(bool, list) # set 信號

    def __init__(self, _model):
        super(AddUnitPage, self).__init__()

        self.ui = Add_Unit_UI.AddUnitPage_UI()
        self.ui.setupUi(self)
        self.model = _model
        self.Initialize()

    # 初始化
    def Initialize(self):
        self.ConnectEvent()

        #Test
        self.ui.textBox_lv1.setText("數學")
        self.ui.textBox_lv2.setText("應用題")
        self.ui.textBox_lv3.setText("典型應用題")
        self.ui.textBox_lv4.setText("燕尾定理")
        self.ui.textBox_lv5.setText("四邊形")

    # 註冊事件
    def ConnectEvent(self):
        self.ui.button_add_unit_confirm.clicked.connect(self.ConfrimAddUnit)
        self.ui.button_add_unit_cancel.clicked.connect(self.CancelAddUnit)

    # 確定新增
    def  ConfrimAddUnit(self):
        tBoxStr_list = [self.ui.textBox_lv1.text(), self.ui.textBox_lv2.text(), self.ui.textBox_lv3.text(), self.ui.textBox_lv4.text(), self.ui.textBox_lv5.text()]
        input_correct = True # 輸入正確
        for tBox in tBoxStr_list:
            if tBox == "":
                input_correct = False

        # 防呆 - 5個都有值
        if input_correct == True:
            check_question_table = self.model.GetQuestionList(tBoxStr_list)
            for list_element in check_question_table:
                print(type(list_element))

            not_have_unit = True
            # 防呆 - 5個都有值 - 且未有單元 - 可正常關閉
            if False:
                is_close = self.close()
                self.add_unit_signal.emit(is_close, tBoxStr_list)
            # 防呆 - 5個都有值 - 已有單元 - 不可關閉
            else:
                QMessageBox.information(self, "警告", "已有此單元!", QMessageBox.Yes)
        # 防呆 - 有1個沒有值 - 不可關閉
        else:
            QMessageBox.information(self, "警告", "單元資訊未填寫完整!", QMessageBox.Yes)

    # 取消新增
    def CancelAddUnit(self):
        is_close = self.close()
        self.add_unit_signal.emit(is_close,[])
