from functools import partial
from PyQt5.QtWidgets import QMainWindow
from model import MyLibrary
from view.UI import Add_Edit_Question_UI
from view import ComboboxView as cbView
import pathlib
import os


class AddEditQuestionPage(QMainWindow):

    comboboxSelectOption = []
    questionList = []

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
        self.ConnectButtonEvent()
        self.LoadComboBox()

    def ConnectButtonEvent(self):
        self.ui.button_add_question.clicked.connect(self.CreateQuestion)
        self.ui.button_import_image.clicked.connect(self.ImportImage)
        self.ui.button_delete_image.clicked.connect(self.DeleteImage)
        self.ui.list_weight_question.currentItemChanged.connect(self.SelectQuestion)

    # 設置下拉是選單內容
    def LoadComboBox(self):
        defaultString = self.comboboxView.GetNoSelectString()
        self.cBoxList[0].addItems(self.comboboxView.GetDictValue(defaultString))

        for i in range(5):
            self.cBoxList[i].activated[str].connect(partial(self.SelectLevel, i))
            self.cBoxList[i].setEditable(True)
            self.cBoxList[i].lineEdit().setText("選擇第" + str(i + 1) + "層")

    # 選取下拉式 - 更新
    def SelectLevel(self, index, text):
        self.UpdateSelectOption(index)  # 更新ComboboxSelectOption = 目前選到的層級 (之後做成key)
        self.UpdateComboBox(index, text)  # 先刪除後面的下拉選單的items再重新加入

        questionType = self.comboboxSelectOption  # 搜尋的條件
        self.questionList = self.model.GetQuestionList(questionType)
        self.LoadQuestionList()

    def ClearCombobox(self):
        self.comboboxSelectOption.clear()
        self.cBoxList[0].addItems(
            self.comboboxView.GetDictValue(self.comboboxView.GetNoSelectString()))  # add default items

        for i in range(1, self.cBoxNum):
            self.cBoxList[i].lineEdit().setText("選擇第" + str(i + 1) + "層")

    def UpdateSelectOption(self, index):
        self.comboboxSelectOption.clear()
        for i in range(index + 1):
            self.comboboxSelectOption.append(self.cBoxList[i].currentText())

    def UpdateComboBox(self, index, text):
        # 更新所選文字
        self.cBoxList[index].setEditText(text)

        # 清除所選之後的選擇
        for i in range(self.cBoxNum - 1, index):
            self.cBoxList[i].clear()
            self.cBoxList[i].lineEdit().setText("選擇第" + str(i + 1) + "層")

        # 非末項，更新後一選項選擇
        if index != self.cBoxNum - 1:
            self.cBoxList[index + 1].addItems(
                self.comboboxView.GetDictValue(MyLibrary.CreateDictKey(self.comboboxSelectOption)))
            self.cBoxList[index + 1].lineEdit().setText("選擇第" + str(index + 2) + "層")

    # 獲取題目表
    def LoadQuestionList(self):
        self.ui.list_weight_question.clear()
        for i in range(len(self.questionList)):
            q_head = str(i) + '. ' + (self.questionList[i].GetQuestion())[:20]
            self.ui.list_weight_question.addItem(q_head)
        # self.ui.list_weight_question.addItems(self.questionList)



    # 真正新增題目
    def AddQuestion(self):
        pass

    # 獲取題目資訊，建立題目類別
    def CreateQuestion(self):
        pass

    # 引入圖片
    def ImportImage(self):
        pass

    # 刪除圖片
    def DeleteImage(self):
        pass

    # 選擇題目 - 更新題目右側資訊
    def SelectQuestion(self, item):
        nowSlectQuestion = item.text()

        # nowSlectIndex = self.ui.list_weight_question.currentIndex()
        # print(nowSlectIndex, type(nowSlectIndex))
        # nowSlectQuestion = self.questionList[nowSlectIndex]

        self.ui.text_edit_question.setPlainText(item.text())
        # self.ui.text_edit_question.setPlainText(nowSlectQuestion.GetQuestion())
        #
        # for i in range(len(self.questionList)):
        #     path = self.questionList[i].GetImage()
        #     img_name = pathlib.PurePath(path).name
        #     self.ui.list_weight_image.addItem(img_name)