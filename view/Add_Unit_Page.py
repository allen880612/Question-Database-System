from functools import partial
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets
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
        self.level = [self.ui.label_lv1, self.ui.label_lv2, self.ui.label_lv3]
        self.tBoxlevel = [self.ui.textBox_lv1, self.ui.textBox_lv2, self.ui.textBox_lv3]
        self.is_click_button = False # 如果透過按下按鈕關閉視窗 這個為True
        self.base_count = 3 # 單元基本上會有的數量
        self.Initialize()

    # 初始化
    def Initialize(self):
        self.ConnectEvent()
        self.UpdateUI()

        self.ui.button_add_level.setEnabled(False)
        #Test
        #self.ui.textBox_lv1.setText("數學")
        #self.ui.textBox_lv2.setText("四邊形")

    # 註冊事件
    def ConnectEvent(self):
        self.ui.button_add_unit_confirm.clicked.connect(self.ConfrimAddUnit)
        self.ui.button_add_unit_cancel.clicked.connect(self.CancelAddUnit)
        self.ui.button_add_level.clicked.connect(self.AddLevel)
        self.ui.button_delete_level.clicked.connect(self.DeleteLevel)

    # ResetPage
    def ResetPage(self):
        self.is_click_button = False
        #self.ui.textBox_lv1.setText("")
        #self.ui.textBox_lv2.setText("")
        #self.ui.textBox_lv3.setText("")
        self.ui.textBox_lv1.setText("")
        self.ui.textBox_lv2.setText("")
        self.ui.textBox_lv3.setText("")
        while self.GetNowLevelNum() > self.base_count:
            self.DeleteLevel()

    # 確定新增
    def  ConfrimAddUnit(self):
        #tBoxStr_list = [self.ui.textBox_lv1.text(), self.ui.textBox_lv2.text(), self.ui.textBox_lv3.text(), self.ui.textBox_lv4.text(), self.ui.textBox_lv5.text()]
        input_correct = True # 輸入正確

        tBoxStr_list = []
        for tBox in self.tBoxlevel:
            tBoxStr_list.append(tBox.text())

        for tBox in tBoxStr_list:
            if tBox == "":
                input_correct = False

        print(tBoxStr_list)

        # 防呆 - 5個都有值
        if input_correct == True:
            check_question_list = self.model.IsPathExist(tBoxStr_list) # 檢查路徑是否存在
            not_have_unit = True
            if check_question_list:
                not_have_unit = False

            # 防呆 - 5個都有值 - 且未有單元 - 可正常關閉
            if not_have_unit:
                self.is_click_button = True
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
        self.is_click_button = True
        is_close = self.close()
        self.add_unit_signal.emit(is_close, [])

    # 新增階層
    def AddLevel(self):
        # add Label
        newLevel = "第 " + str(self.GetNowLevelNum() - 1) + " 層"
        newLabelName = "label_lv" + str(self.GetNowLevelNum() + 1)
        newLabel = QtWidgets.QLabel(self.ui.centralwidget)
        newLabel.setAlignment(QtCore.Qt.AlignCenter)
        newLabel.setObjectName(newLabelName)
        newLabel.setText("單元") # 交換單元 以及 新增的階層的文字內容
        self.level[-1].setText(newLevel)
        self.ui.gridLayout_3.addWidget(newLabel, 0, self.GetNowLevelNum(), 1, 1)
        
        # add textbox
        newtBoxName = "textBox_lv" + str(self.GetNowLevelNum() + 1)
        newtBox = QtWidgets.QLineEdit(self.ui.centralwidget)
        newtBox.setAlignment(QtCore.Qt.AlignCenter)
        newtBox.setObjectName(newtBoxName)
        newtBox.setText("")
        self.ui.gridLayout_3.addWidget(newtBox, 2, self.GetNowLevelNum(), 1, 1)

        # add level
        self.level.append(newLabel)
        self.tBoxlevel.append(newtBox)
        self.UpdateUI()

    # 刪除階層
    def DeleteLevel(self):
        self.ui.gridLayout_3.removeWidget(self.level[-1])
        self.ui.gridLayout_3.removeWidget(self.tBoxlevel[-1])

        self.level[-1].setVisible(False)
        self.tBoxlevel[-1].setVisible(False)

        self.level.pop()
        self.tBoxlevel.pop()
        
        self.level[-1].setText("單元")
        self.UpdateUI()

    # 取得目前階層數
    def GetNowLevelNum(self):
        return len(self.level)

    # 更新UI
    def UpdateUI(self):
        self.ui.button_delete_level.setEnabled(self.GetNowLevelNum() > self.base_count)
    
    # 關閉視窗事件
    def closeEvent(self, event):
        # 不是透過按鈕來關閉視窗 > 同關閉
        if self.is_click_button == False:
            is_close = True
            self.add_unit_signal.emit(is_close, [])