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
        # ui層
        self.listWidget_question_level = self.ui.listWidget_make_question_level
        self.listWidget_none_select_question = self.ui.listWidget_none_select_question
        self.listWidget_selected_question = self.ui.listWidget_selected_question
        self.preview_question_content = self.ui.textEdit_preview_question

        # 前幾層所選之題目階層 (tuple list: level, question number)
        self.question_level_tupleList = []

        # 未選擇到的題目dict (key: level, value: node list)
        self.question_nonSelect_dict = {}

        # 選擇到的題目dict (key: level, value: node list)
        self.question_select_dict = {}

        self.Initialize()

    # 初始化
    def Initialize(self):
        self.ConnectEvent()
        self.ResetPage()

    # 重設頁面
    def ResetPage(self):
        self.is_click_button = False

        level_list = [level[0] for level in self.question_level_tupleList]
        number_list = [number[1] for number in self.question_level_tupleList]
        self.UpdateListWidget(self.listWidget_question_level, [MyLibrary.GetQuestionShowText(level) for level in level_list])
        self.listWidget_none_select_question.clear()
        self.listWidget_selected_question.clear()

        self.InitializeDict()
        self.UpdateUI()

    # 註冊事件
    def ConnectEvent(self):
        self.ui.button_return.clicked.connect(self.ClosePage)
        self.ui.listWidget_make_question_level.currentItemChanged.connect(self.SelectQuestionLevel)
        self.ui.listWidget_none_select_question.currentItemChanged.connect(lambda: self.SelectQuestion(0))
        self.ui.listWidget_selected_question.currentItemChanged.connect(lambda: self.SelectQuestion(1))

        self.ui.button_add_question.clicked.connect(self.AddToMakeQuestionList)
        self.ui.button_remove_question.clicked.connect(self.RemoveFromMakeQuestionList)

    # 刷新UI
    def UpdateUI(self):
        self.ui.button_remove_question.setEnabled(self.listWidget_selected_question.currentRow() > -1)
        self.ui.button_add_question.setEnabled(self.listWidget_none_select_question.currentRow() > -1)

    # 更新 listwidget
    def UpdateListWidget(self, list_widget, data_list):
        list_widget.clear()
        list_widget.addItems(data_list)

    # 更新 未選擇題目的 list widget
    def UpdateNoneSelectQuestionListWidget(self):
        preview_question_count = 15

        level_key = self.GetLevelKey()

        # 建構 未選擇的題目
        tmp_nonSelectQuestion_list = []
        for question in self.question_nonSelect_dict[level_key]:
            tmp_nonSelectQuestion_list.append(question.GetQuestion()[:preview_question_count])
        self.UpdateListWidget(self.listWidget_none_select_question, tmp_nonSelectQuestion_list)

    # 更新 已選擇題目的 list widget
    def UpdateSelectQuestionListWidget(self):
        preview_question_count = 15

        level_key = self.GetLevelKey()

        # 建構 已選擇的題目
        tmp_selectQuestion_list = []
        for question in self.question_select_dict[level_key]:
            tmp_selectQuestion_list.append(question.GetQuestion()[:preview_question_count])
        self.UpdateListWidget(self.listWidget_selected_question, tmp_selectQuestion_list)

    # 初始化字典
    def InitializeDict(self):
        self.question_nonSelect_dict.clear()
        self.question_select_dict.clear()

        #level_list = [level[0] for level in self.question_level_tupleList]
        #number_list = [number[1] for number in self.question_level_tupleList]

        for level, number in self.question_level_tupleList:
            keys = MyLibrary.CreateDictKey(level)
            qList = self.model.GetQuestionList(keys)

            # 一階初始化
            self.question_nonSelect_dict[keys] = []
            self.question_select_dict[keys] = []

            number_list = [i for i in range(0, len(qList))] # 取得0 ~ len(qList)的數字陣列
            number_list = random.sample(number_list, min(number, len(qList))) # 取得不重複 (number) 個題
            
            # 開建
            for qIndex in range(0, len(qList)):
                if qIndex in number_list: # 被選到
                    self.question_select_dict[keys].append(qList[qIndex])
                else:
                    self.question_nonSelect_dict[keys].append(qList[qIndex])

    # 選擇 題目階層
    def SelectQuestionLevel(self, item):
        preview_question_count = 15
        current_row = self.listWidget_question_level.currentRow()
        if current_row == -1:
            return

        level_key = self.GetLevelKey()

        # 更新 未選擇的題目的 List Widget
        self.UpdateNoneSelectQuestionListWidget()

        # 更新 已選擇的題目的 List Widget
        self.UpdateSelectQuestionListWidget()

        self.UpdateUI()
    
    # 選擇題目
    def SelectQuestion(self, case):
        list_widget = self.sender()
        current_row = list_widget.currentRow()
        if current_row == -1:
            return

        level_key = self.GetLevelKey()

        if case == 0:
            tmp_text = self.question_nonSelect_dict[level_key][current_row].GetQuestionAnswer()
            self.preview_question_content.setText(tmp_text)
            self.listWidget_selected_question.setCurrentRow(-1)
        elif case == 1:
            tmp_text = self.question_select_dict[level_key][current_row].GetQuestionAnswer()
            self.preview_question_content.setText(tmp_text)
            self.listWidget_none_select_question.setCurrentRow(-1)

        self.UpdateUI()

    # 加入到出題列表
    def AddToMakeQuestionList(self):
        current_row = self.listWidget_none_select_question.currentRow()
        if current_row == -1:
            return

        level_key = self.GetLevelKey()

        select_question = self.question_nonSelect_dict[level_key][current_row] # 取得題目
        self.question_select_dict[level_key].append(select_question) # 已選擇題目 增加一筆
        self.question_nonSelect_dict[level_key].remove(select_question) # 未選擇題目 刪除這筆
        self.listWidget_none_select_question.setCurrentRow(-1) # 取消Focus
        
        # 更新 未選擇的題目的 List Widget
        self.UpdateNoneSelectQuestionListWidget()
        # 更新 已選擇的題目的 List Widget
        self.UpdateSelectQuestionListWidget()
        
    # 從出題列表中移除
    def RemoveFromMakeQuestionList(self):
        current_row = self.listWidget_selected_question.currentRow()
        if current_row == -1:
            return

        level_key = self.GetLevelKey()

        select_question = self.question_select_dict[level_key][current_row] # 取得題目
        self.question_nonSelect_dict[level_key].append(select_question) # 未選擇題目 增加一筆
        self.question_select_dict[level_key].remove(select_question) # 已選擇題目 刪除這筆
        self.listWidget_selected_question.setCurrentRow(-1) # 取消Focus

        # 更新 未選擇的題目的 List Widget
        self.UpdateNoneSelectQuestionListWidget()
        # 更新 已選擇的題目的 List Widget
        self.UpdateSelectQuestionListWidget()

    # 取得用於字典查詢時的level -> type = tuple
    def GetLevelKey(self):
        level = self.question_level_tupleList[self.listWidget_question_level.currentRow()][0]
        level_key = MyLibrary.CreateDictKey(level)
        return level_key

    # 設置必要的資料 
    def SetQuestionLevelTupleData(self, tuple_list):
        self.question_level_tupleList = tuple_list

    # 關閉這個視窗
    def ClosePage(self):
        self.is_click_button = True
        is_close = self.close()
        self.revise_make_question_signal.emit(is_close)

    # 關閉視窗事件
    def closeEvent(self, event):
        self.question_level_tupleList = []
        if self.is_click_button == False:
            is_close = True
            self.revise_make_question_signal.emit(is_close)