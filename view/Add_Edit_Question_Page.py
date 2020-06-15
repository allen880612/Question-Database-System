from functools import partial
from PyQt5.QtWidgets import QMainWindow
from model import MyLibrary
from view.UI import Add_Edit_Question_UI
from view import ComboboxView as cbView
import pathlib
import copy
import os


class AddEditQuestionPage(QMainWindow):

    comboboxSelectOption = []
    questionList = []
    MODE_ADD_QUESTION = "add_question"
    MODE_EDIT_QUESTION = "edit_question"
    mode = ""

    def __init__(self, _model):
        super(AddEditQuestionPage, self).__init__()

        self.ui = Add_Edit_Question_UI.AddEditQuestionPage_UI()
        self.ui.setupUi(self)

        self.model = _model
        self.comboboxView = cbView.ComboboxView(self.model.GetOriginalDataFrame())
        self.cBoxList = [self.ui.cBox_lv1, self.ui.cBox_lv2, self.ui.cBox_lv3, self.ui.cBox_lv4, self.ui.cBox_lv5]
        self.cBoxNum = len(self.cBoxList)

        self.Initialize()

    def Initialize(self):
        self.ConnectEvent()
        self.LoadComboBox()
        self.InitUI()
        self.UpdateUI()
        self.mode = self.MODE_ADD_QUESTION

    def ConnectEvent(self):
        self.ui.button_add_question.clicked.connect(self.CreateQuestion)
        self.ui.button_import_image.clicked.connect(self.ImportImage)
        self.ui.button_delete_image.clicked.connect(self.DeleteImage)
        self.ui.list_weight_question.currentItemChanged.connect(self.SelectQuestion)
        self.ui.text_edit_question.textChanged.connect(self.UpdateUI)
        self.ui.button_edit_question_mode.clicked.connect(self.ClickEditMode)
        self.ui.button_add_question_mode.clicked.connect(self.ClickAddMode)

    def InitUI(self):
        # 預設為新增模式
        self.ui.button_add_question_mode.setEnabled(False)
        self.ui.button_edit_question_mode.setEnabled(True)

    # 設置下拉是選單內容
    def LoadComboBox(self):
        defaultString = self.comboboxView.GetNoSelectString()
        self.cBoxList[0].addItems(self.comboboxView.GetDictValue(defaultString))

        for i in range(5):
            self.cBoxList[i].activated[str].connect(partial(self.SelectComboBox, i))
            self.cBoxList[i].setEditable(True)
            self.cBoxList[i].lineEdit().setText("選擇第" + str(i + 1) + "層")

    # 新增按鈕是否可以按下
    def GetAddButtonEnable(self):
        flag = True
        # print(f"text={not len(self.ui.text_edit_question.toPlainText()) == 0}")
        flag &= (not len(self.ui.text_edit_question.toPlainText()) == 0)
        # print(f"cBox={len(self.comboboxSelectOption) == self.cBoxNum}")
        flag &= (len(self.comboboxSelectOption) == self.cBoxNum)
        # print(f"flag={flag}")
        return flag

    # 編輯按鈕是否可以按下
    def GetEditButtonEnable(self):
        flag = True
        # print(f"text={not len(self.ui.text_edit_question.toPlainText()) == 0}")
        flag = flag and (not len(self.ui.text_edit_question.toPlainText()) == 0)
        # print(f"cBox={len(self.comboboxSelectOption) == self.cBoxNum}")
        flag = flag and (len(self.comboboxSelectOption) == self.cBoxNum)
        print(f"flag={flag}")
        return flag

    # 更新UI
    def UpdateUI(self):
        # 空白題目 不該被新增 /修改
        self.ui.button_add_question.setEnabled(self.GetAddButtonEnable())

    # 選取下拉式 - 更新
    def SelectComboBox(self, index, text):
        self.UpdateSelectOption(index)  # 更新ComboboxSelectOption = 目前選到的層級 (之後做成key)
        self.UpdateComboBox(index, text)  # 先刪除後面的下拉選單的items再重新加入
        self.UpdateUI()
        self.LoadQuestionList()

    # 切換至編輯模式
    def ClickEditMode(self):
        self.ui.button_edit_question_mode.setEnabled(False)
        self.ui.button_add_question_mode.setEnabled(True)
        self.mode = self.MODE_EDIT_QUESTION
        self.ui.list_weight_image.clear()
        self.LoadQuestionList()

    # 切換至新增模式
    def ClickAddMode(self):
        self.ui.button_edit_question_mode.setEnabled(True)
        self.ui.button_add_question_mode.setEnabled(False)
        self.mode = self.MODE_ADD_QUESTION
        self.ui.text_edit_question.clear()
        self.ui.list_weight_image.clear()
        self.ui.list_weight_question.clear()

    # 清除所有下拉式選單內容
    def ClearCombobox(self):
        self.comboboxSelectOption.clear()
        self.cBoxList[0].addItems(
            self.comboboxView.GetDictValue(self.comboboxView.GetNoSelectString()))  # add default items

        for i in range(1, self.cBoxNum):
            self.cBoxList[i].lineEdit().setText("選擇第" + str(i + 1) + "層")

    # 更新篩選題目list (由下拉式選單選中選像)
    def UpdateSelectOption(self, index):
        self.comboboxSelectOption.clear()
        for i in range(index + 1):
            self.comboboxSelectOption.append(self.cBoxList[i].currentText())
        print(self.comboboxSelectOption)

    # 更新下拉式選單 (由前個 更新後個)
    def UpdateComboBox(self, index, text):
        # 更新所選文字
        self.cBoxList[index].setEditText(text)

        # 清除所選之後的選擇
        for i in range(self.cBoxNum - 1, index):
            self.cBoxList[i].clear()
            self.cBoxList[i].lineEdit().setText("選擇第" + str(i + 1) + "層")

        # 非末項，更新後一選項選擇
        if index != self.cBoxNum - 1:
            key = MyLibrary.CreateDictKey(self.comboboxSelectOption)
            nextLevelItems = self.comboboxView.GetDictValue(key)

            # 若回傳 None， 為使用者手動輸入，用於新增題目
            if not nextLevelItems:
                pass
            else:
                self.cBoxList[index + 1].clear()
                self.cBoxList[index + 1].addItems(nextLevelItems)
                self.cBoxList[index + 1].lineEdit().setText("選擇第" + str(index + 2) + "層")

    # 獲取題目表
    def LoadQuestionList(self):
        if self.mode == self.MODE_ADD_QUESTION:
            return
        questionType = self.comboboxSelectOption  # 搜尋的條件
        self.questionList = self.model.GetQuestionList(questionType)
        self.ui.list_weight_question.clear()
        for i in range(len(self.questionList)):
            q_head = str(i) + '. ' + (self.questionList[i].GetQuestion())[:20]
            self.ui.list_weight_question.addItem(q_head)
        # self.ui.list_weight_question.addItems(self.questionList)

    # 真正新增題目
    def AddQuestion(self, dict_q):
        self.model.AddQuestion(dict_q)
        self.ui.text_edit_question.clear()
        self.ui.list_weight_image.clear()

    # 獲取題目資訊，建立題目類別
    def CreateQuestion(self):
        q_info = copy.deepcopy(self.comboboxSelectOption)
        q_info.append(len(self.questionList) + 2)
        q_info.append(self.ui.text_edit_question.toPlainText())
        q_info.append("NOIMAGE")
        dict_q = dict(zip(self.model.GetOriginalDataFrame().columns, q_info))
        # print(dict_q)
        self.AddQuestion(dict_q)

    # 引入圖片
    def ImportImage(self):
        pass

    # 刪除圖片
    def DeleteImage(self):
        pass

    # 選擇題目 - 更新題目右側資訊
    def SelectQuestion(self, item):
        # nowSlectQuestion = item.text()
        # self.ui.text_edit_question.setPlainText(item.text())

        nowSlectIndex = self.ui.list_weight_question.currentRow()
        # print(nowSlectIndex, type(nowSlectIndex))
        if self.mode == self.MODE_ADD_QUESTION or nowSlectIndex == -1:
            return

        nowSlectQuestion = self.questionList[nowSlectIndex]
        self.ui.text_edit_question.setPlainText(nowSlectQuestion.GetQuestionAnswer())

        text = str(self.ui.text_edit_question.toPlainText())
        print(type(text), text)

        self.ui.list_weight_image.clear()
        path = nowSlectQuestion.GetImage()

        if path:
            for p in path:
                img_name = pathlib.PurePath(p).name
                self.ui.list_weight_image.addItem(img_name)