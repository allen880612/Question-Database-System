from functools import partial
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets
from model import MyLibrary
from model import QtExtend
from view.UI import Select_Question_UI
from view import ComboboxView as cbView
import pathlib
import os
import copy

class SelectQuestionPage(QMainWindow):
    
    #add_unit_signal = QtCore.pyqtSignal(bool, list) # set 信號

    def __init__(self, _model):
        super(SelectQuestionPage, self).__init__()

        self.ui = Select_Question_UI.SelectQuestion_UI()
        self.ui.setupUi(self)
        self.model = _model

        self.comboboxView = cbView.ComboboxView(self.model)

        # 題目階層的Layout
        self.questionLevelLayout = [self.ui.verticalLayout_lv1, self.ui.verticalLayout_lv2, self.ui.verticalLayout_lv3, self.ui.verticalLayout_lv4, self.ui.verticalLayout_lv5]
        # 每個layout有幾個checkbox
        self.layoutLevelCount = [0, 0, 0, 0, 0]
        # 查詢用check box dict
        self.checkboxDict = {}


        self.Initialize()

    # 初始化
    def Initialize(self):
        self.ConnectEvent()
        self.ResetPage()
        self.UpdateUI()

    # 註冊事件
    def ConnectEvent(self):
        self.ui.button_add_question.clicked.connect(self.zzxcv)

    # ResetPage
    def ResetPage(self):
        self.questionLevelLayout = [self.ui.verticalLayout_lv1, self.ui.verticalLayout_lv2, self.ui.verticalLayout_lv3, self.ui.verticalLayout_lv4, self.ui.verticalLayout_lv5]
        self.checkboxDict = {}
        create_checkbox_list = self.comboboxView.GetDictValue("NOSELECT")
        for checkbox_text in create_checkbox_list:
            checkbox_name = self.CreateCheckboxObjectName(0)
            self.AddCheckbox(checkbox_text, checkbox_name, 0, [])

    # 確定新增
    def  ConfrimAddUnit(self):
       pass

    # 取消新增
    def CancelAddUnit(self):
        pass

    # 新增階層
    def AddLevel(self):
        pass

    # 刪除階層
    def DeleteLevel(self):
        pass

    # 取得目前階層數
    def GetNowLevelNum(self):
        pass

    # 更新UI
    def UpdateUI(self):
        pass

    def zzxcv(self):
        self.AddCheckbox("fuck", "checkbox_lv1_1", 0)
        
    # Add check box (顯示文字, checkbox物件名稱, layout第幾層, 問題的層路徑)
    def AddCheckbox(self, show_text, checkbox_name, layoutLevel, preQuestionLevel):
        new_checkbox = QtWidgets.QCheckBox(self.ui.centralwidget)
        new_checkbox.setText(show_text)
        new_checkbox.setObjectName(checkbox_name)
        self.questionLevelLayout[layoutLevel].addWidget(new_checkbox, 0, QtCore.Qt.AlignTop)
        new_checkbox.clicked.connect(self.ClickedCheckBox)

        new_questionLevel = copy.deepcopy(preQuestionLevel)
        new_questionLevel.append(show_text)
        self.checkboxDict[checkbox_name] = QtExtend.CheckboxData(new_checkbox, self.questionLevelLayout[layoutLevel], layoutLevel, new_questionLevel)
        self.layoutLevelCount[layoutLevel] += 1

    # 點選 checkbox
    def ClickedCheckBox(self):
        cbox = self.sender()
        cbox_data = self.FindCheckbox(cbox.objectName())

        # 被選中
        if cbox.isChecked():
            next_level_list = self.comboboxView.GetDictValue(self.GetQuestionLevelTupleKey(cbox_data.questionLevel))
            preLevel = copy.deepcopy(cbox_data.questionLevel)
            print("nextlevel=")
            print(next_level_list)
            for checkbox_text in next_level_list:
                checkbox_name = self.CreateCheckboxObjectName(cbox_data.layoutLevel + 1)
                self.AddCheckbox(checkbox_text, checkbox_name, cbox_data.layoutLevel + 1, preLevel)

        # 沒被選中
        elif not cbox.isChecked():
            print("雞雞")
    
    # 創造Checkbox name (checkbox_lv0_0)
    def CreateCheckboxObjectName(self, layout_level):
        return "checkbox_lv" + str(layout_level) + "_" + str(self.layoutLevelCount[layout_level])

    # 查詢字典中的Check box
    def FindCheckbox(self, checkbox_name):
        return self.checkboxDict.get(checkbox_name)

    # 取得 篩選comboboxView.GetDictValue 用的tuple key
    def GetQuestionLevelTupleKey(self, questionLevel):
        if len(questionLevel) == 1:
            return questionLevel[0]
        else:
            return tuple(questionLevel)