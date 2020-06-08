from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow
from view.UI import AddQuestion
import os

class Craeate_question(QMainWindow):

    def __init__(self,):
        super(Craeate_question, self).__init__()

        self.ui = AddQuestion.Add_question_UI()
        self.ui.setupUi(self)
        self.Initialize()

    def Initialize(self):
        self.ConnectButtonEvent()
        self.LoadComboBox()

    def ConnectButtonEvent(self):
        self.ui.button_add_question.clicked.connect(self.CreateQuestion)
        self.ui.button_import_image.clicked.connect(self.ImportImage)
        self.ui.button_delete_image.clicked.connect(self.DeleteImage)
        self.ui.list_weight_question.itemChanged.connect(self.SelectQuestion)
        # self.ui.comboBox_question_0.currentIndexChanged.connect(self.SelectLevel_0)

    # 設置下拉是選單內容
    def LoadComboBox(self):
        pass

    # 獲取題目表
    def LoadQuestionList(self):
        pass

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
    def SelectQuestion(self):
        pass