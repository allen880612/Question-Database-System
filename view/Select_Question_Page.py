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
        # 查詢用check box dict
        self.checkboxDict = {}
        # verticalLayout Dict (收集checkbox)
        self.layoutDict = {} 

        # Question Level Tree
        self.QLT = QtExtend.QLT(self.comboboxView)
        self.QLT.CreateTree()
        self.QLT.DFS()

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
        
        # reset layout dict
        self.layoutDict = {}
        self.layoutDict[self.ui.verticalLayout_lv1] = []
        self.layoutDict[self.ui.verticalLayout_lv2] = []
        self.layoutDict[self.ui.verticalLayout_lv3] = []
        self.layoutDict[self.ui.verticalLayout_lv4] = []
        self.layoutDict[self.ui.verticalLayout_lv5] = []

        # reset checkbox dict
        self.checkboxDict = {}
        #create_checkbox_list = self.comboboxView.GetDictValue("NOSELECT")
        #for checkbox_text in create_checkbox_list:
        #    checkbox_name = self.CreateCheckboxObjectName(0)
        #    self.AddCheckbox(checkbox_text, checkbox_name, 0, [])
        show_QTLNode_list = self.QLT.GetNodeByLevel(0)
        for node in show_QTLNode_list:
            checkbox_name = self.CreateCheckboxObjectName(0)
            self.AddCheckbox(node.name, checkbox_name, 0, [])

        # test
        node = self.QLT.GetNodeByQuestionLevel(["數學", "應用題", "典型應用題", "燕尾定理"])
        if node == None:
            print("fuck")
        else:
            print(node.depth)
            print(node.questionLevel)

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
    
    # 重設該Layout
    def ResetLayout(self, layout_level):
        show_QTLNode_list = self.QLT.GetNodeByLevel(layout_level)
        layout = self.questionLevelLayout[layout_level]
        for node in show_QTLNode_list:
            if node.isShow:
                checkbox_name = self.CreateCheckboxObjectName(layout_level)
                preList = copy.deepcopy(node.questionLevel)
                preList.pop()
                self.AddCheckbox(node.name, checkbox_name, layout_level, preList, node.isCheck)

    # 刪除 layout 所有的element (checkbox)
    def DeleteLayoutElement(self, layout):
        del_layoutElement_list = self.layoutDict[layout]
        for del_cbox in del_layoutElement_list:
            self.DeleteCheckbox(del_cbox)
        self.layoutDict[layout].clear()

    # Add check box (顯示文字, checkbox物件名稱, layout第幾層, 問題的層路徑, 有是否被勾選)
    def AddCheckbox(self, show_text, checkbox_name, layoutLevel, preQuestionLevel, isCheck=False):
        currentLayout = self.questionLevelLayout[layoutLevel] # 目前layout
        new_checkbox = QtWidgets.QCheckBox(self.ui.centralwidget)
        new_checkbox.setText(show_text)
        new_checkbox.setObjectName(checkbox_name)
        new_checkbox.setChecked(isCheck)
        currentLayout.addWidget(new_checkbox, 0, QtCore.Qt.AlignTop)
        new_checkbox.clicked.connect(self.ClickedCheckBox)

        new_questionLevel = copy.deepcopy(preQuestionLevel) # question level
        new_questionLevel.append(show_text)
        self.checkboxDict[checkbox_name] = QtExtend.CheckboxData(new_checkbox, currentLayout, layoutLevel, new_questionLevel)
        self.layoutDict[currentLayout].append(new_checkbox)

    # 刪除Checkbox (被刪除的checkbox)
    def DeleteCheckbox(self, del_checkbox):
        cbox_data = self.FindCheckbox(del_checkbox.objectName())
        del_checkbox.setVisible(False)
        cbox_data.layout.removeWidget(del_checkbox)
        # self.layoutDict[cbox_data.layout].remove(del_checkbox)
        del self.checkboxDict[del_checkbox.objectName()]

    # 點選 checkbox
    def ClickedCheckBox(self):
        cbox = self.sender()
        cbox_data = self.FindCheckbox(cbox.objectName())

        ## 被選中
        if cbox.isChecked():
            self.SelectCheckBox(cbox, cbox_data)

        ## 沒被選中
        elif not cbox.isChecked():
            self.CancelSelectCheckBox(cbox, cbox_data)
    
    # 勾選 CheckBox (cbox = 被勾選的checkbox, cbox_data = 他的資料)
    def SelectCheckBox(self, cbox, cbox_data):
        print("quesetion: ", cbox_data.questionLevel)

        node = self.QLT.GetNodeByQuestionLevel(cbox_data.questionLevel) # 取得node
        node.isCheck = True
        # 非葉節點才更新 & 重建
        if len(node.childList) != 0:
            # 更新 QLT
            for child in node.childList:
                child.isShow = True
        
            # 重建layout
            reset_depth = cbox_data.layoutLevel + 1
            self.DeleteLayoutElement(self.questionLevelLayout[reset_depth])
            self.ResetLayout(reset_depth)

    # 取消勾選 CheckBox (cbox = 被勾選的checkbox, cbox_data = 他的資料)
    def CancelSelectCheckBox(self, cbox, cbox_data):
        # 更新 QLT
        node = self.QLT.GetNodeByQuestionLevel(cbox_data.questionLevel)
        node.isCheck = False
        for child in node.childList:
            self.QLT.SetTreeCheckShow(child, False)
        
        this_depth = cbox_data.layoutLevel
        # 重建Layout
        for layout_level in range(this_depth + 1, len(self.questionLevelLayout)):
            self.DeleteLayoutElement(self.questionLevelLayout[layout_level])
            self.ResetLayout(layout_level)

    # 創造Checkbox name (checkbox_lv0_0)
    def CreateCheckboxObjectName(self, layout_level):
        currentLayout = self.questionLevelLayout[layout_level]
        return "checkbox_lv" + str(layout_level) + "_" + str(len(self.layoutDict.get(currentLayout)))

    # 查詢字典中的Check box
    def FindCheckbox(self, checkbox_name):
        return self.checkboxDict.get(checkbox_name)

    # 取得 篩選comboboxView.GetDictValue 用的tuple key
    def GetQuestionLevelTupleKey(self, questionLevel):
        if len(questionLevel) == 1:
            return questionLevel[0]
        else:
            return tuple(questionLevel)