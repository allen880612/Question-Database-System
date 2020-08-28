from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from model import MyLibrary
from view.UI import Add_Edit_Question_UI
from view import Add_Unit_Page
import PIL
import pathlib
import copy
import os

class AddEditQuestionPage(QMainWindow):

    comboboxSelectOption = []
    questionList = []
    imageListPath = []
    MODE_ADD_QUESTION = "add_question"
    MODE_EDIT_QUESTION = "edit_question"
    MODE_FILLING_QUESTION = "FillingQuestion_Mode"
    MODE_SELECT_QUESTION = "SelectQuestion_Mode"
    mode = ""
    question_mode = ""
    #Add_Unit_View = "" 
    Is_add_unit_view_open = False

    # 建構子
    def __init__(self, _model):
        super(AddEditQuestionPage, self).__init__()

        self.ui = Add_Edit_Question_UI.AddEditQuestionPage_UI()
        self.ui.setupUi(self)

        self.model = _model

        # 上一層所選的level的list
        self.question_level_list = []
        
        # 這一頁所使用的question level (self.question_level_list[0])
        self.question_level = []

        # temp import Image
        self.temp_importImage = None

        # 圖片List
        self.imageList = []

        # 特立獨行的Select Question
        self.tmp_SelectQuestion = MyLibrary.SelectQuestion(0, "")

        # 選擇題模式中選到哪個部分 (問題? 答案? 選項?)
        self.select_question_edit_what = ""

        # 編輯的問題
        self.editQuestion = None

        #region 新增單元 視窗 變數 (移到主畫面)
        #self.Add_Unit_View = Add_Unit_Page.AddUnitPage(self.model)
        #self.Add_Unit_View.setWindowModality(Qt.ApplicationModal)
        #endregion

        self.Initialize()

    # 初始化
    def Initialize(self):
        self.ConnectEvent()
        self.ResetPage()
        self.UpdateUI()
        self.mode = self.MODE_ADD_QUESTION

    # 註冊事件
    def ConnectEvent(self):
        self.ui.button_add_question.clicked.connect(self.ClickAddQuestionButton) # Link 新增題目按鈕
        self.ui.button_import_image.clicked.connect(self.ImportImage)
        self.ui.button_addToList_image.clicked.connect(self.AddToImageList)
        self.ui.button_delete_image.clicked.connect(self.DeleteImage)
        self.ui.list_weight_question.currentItemChanged.connect(self.SelectQuestion)
        self.ui.list_widget_option.currentItemChanged.connect(self.SelectOption)
        self.ui.text_edit_question.textChanged.connect(self.UpdateUI)
        self.ui.button_edit_question_mode.clicked.connect(self.ClickEditMode)
        self.ui.button_add_question_mode.clicked.connect(self.ClickAddMode)
        self.ui.list_weight_image.currentItemChanged.connect(self.SelectImage) # 選擇圖片
        
        self.ui.radioButton_FillingQuestion.toggled.connect(self.ClickFillingQuestionMode)
        self.ui.radioButton_SelectQuestion.toggled.connect(self.ClickSelectQuestionMode)

        self.ui.button_add_option.clicked.connect(self.ClickAddOptionButton)
        self.ui.button_remove_option.clicked.connect(self.ClickRemoveOptionButton)

        self.ui.text_edit_question.textChanged.connect(lambda: self.InputTextEdit(self.ui.text_edit_question))

        # 新增單元 視窗 (移到選擇路徑畫面)
        # self.ui.button_add_unit.clicked.connect(self.OpenAddUnitView)
        # self.Add_Unit_View.add_unit_signal.connect(self.GetADdUnitViewData)

    # 重設頁面
    def ResetPage(self):
        defaultString = self.model.DefaultString_NoSelect
        self.question_mode = ""
        self.ClickAddMode()
        self.ui.radioButton_FillingQuestion.click()
        self.ui.label_question_level.setText(MyLibrary.GetQuestionShowText(self.question_level))
        self.mode = self.MODE_ADD_QUESTION

    # 新增按鈕是否可以按下
    def GetAddQuestionButtonEnable(self):
        return len(self.ui.text_edit_question.toPlainText()) != 0

    # 編輯按鈕是否可以按下
    def GetEditButtonEnable(self):
        return True

    # 新增題目模式 按鈕 是否可以被按下
    def IsAddModeButtonEnable(self):
        return self.mode != self.MODE_ADD_QUESTION

    # 編輯題目模式 按鈕 是否可以被按下
    def IsEditModeButtonEnable(self):
        return self.mode != self.MODE_EDIT_QUESTION

    # 更新UI
    def UpdateUI(self):
        # 空白題目 不該被新增 / 修改
        self.ui.button_add_question.setEnabled(self.GetAddQuestionButtonEnable())
        # 未選擇單元 不該能修改
        self.ui.button_edit_question_mode.setEnabled(self.GetEditButtonEnable())
        # 未引入圖片 不能新增
        self.ui.button_addToList_image.setEnabled(self.temp_importImage != None)

        # 切換模式按鈕
        self.ui.button_add_question_mode.setEnabled(self.IsAddModeButtonEnable())
        self.ui.button_edit_question_mode.setEnabled(self.IsEditModeButtonEnable())

    # 每次切換操作後，重設UI
    def ResetUI(self):
        pass

    # 切換至編輯模式
    def ClickEditMode(self):
        self.mode = self.MODE_EDIT_QUESTION
        self.editQuestion = None
        self.ui.list_weight_image.clear()
        self.imageList.clear()
        temp_importImage = None
        self.LoadQuestionList()
        self.ui.label_image_preview.clear() # 清空預覽圖片
        self.ui.button_add_question.setText("儲存題目")
        # 取消顯示兩個radio button
        self.ui.radioButton_FillingQuestion.setVisible(False)
        self.ui.radioButton_SelectQuestion.setVisible(False)
        self.UpdateUI()

    # 切換至新增模式
    def ClickAddMode(self):
        self.mode = self.MODE_ADD_QUESTION
        self.editQuestion = None
        self.ui.text_edit_question.clear()
        self.ui.list_weight_image.clear()
        self.imageList.clear()
        temp_importImage = None
        self.ui.list_weight_question.clear()
        self.LoadQuestionList()
        self.ui.label_image_preview.clear() # 清空預覽圖片
        self.ui.button_add_question.setText("新增題目")
        # 顯示兩個radio button
        self.ui.radioButton_FillingQuestion.setVisible(True)
        self.ui.radioButton_SelectQuestion.setVisible(True)
        self.ui.radioButton_FillingQuestion.click()
        self.UpdateUI()

    # 切換至填充題模式
    def ClickFillingQuestionMode(self):
        if self.question_mode != self.MODE_FILLING_QUESTION:
            self.question_mode = self.MODE_FILLING_QUESTION
            self.SetFillingQuestionMode()

            self.ui.text_edit_question.clear()
            self.tmp_SelectQuestion = None
    # 切換至選擇題模式
    def ClickSelectQuestionMode(self):
        if self.question_mode != self.MODE_SELECT_QUESTION:
            self.question_mode = self.MODE_SELECT_QUESTION
            self.select_question_edit_what = ""

            self.ui.text_edit_question.clear()
            self.SetSelectQuestionMode()

            self.ui.list_weight_question.clear()
            self.ui.list_weight_question.addItem("question")
            self.tmp_SelectQuestion = MyLibrary.SelectQuestion(0, "") # 重設新增選擇題題題
            for i in range(4):
                self.ClickAddOptionButton()

    # 設置成 填充題模式
    def SetFillingQuestionMode(self):
        self.ui.label.setVisible(False)
        self.ui.list_widget_option.setVisible(False)
        self.ui.button_add_option.setVisible(False)
        self.ui.button_remove_option.setVisible(False)

        self.ui.list_weight_question.clear()

    # 設置成 選擇題模式
    def SetSelectQuestionMode(self):
        self.ui.label.setVisible(True)
        self.ui.list_widget_option.setVisible(True)
        self.ui.button_add_option.setVisible(True)
        self.ui.button_remove_option.setVisible(True)

        self.ui.list_widget_option.clear()

    # 點擊 新增題目 按鈕
    def ClickAddQuestionButton(self):
        if self.mode == self.MODE_ADD_QUESTION:
            self.AddQuestion()
        elif self.mode == self.MODE_EDIT_QUESTION:
            self.StoreQuestion()

    # 點擊新增選項按鈕
    def ClickAddOptionButton(self):
        id = int(self.ui.list_widget_option.count() + 1)
        self.ui.list_widget_option.addItem(str(id))
        self.ui.list_widget_option.item(id - 1).setCheckState(False)
        if self.tmp_SelectQuestion is not None:
            self.tmp_SelectQuestion.AddOption(id)

    # 點擊移除選項按鈕
    def ClickRemoveOptionButton(self):
        nowSelectIndex = self.ui.list_widget_option.currentRow()
        
        if nowSelectIndex == -1:
            return
        
        for i in range(nowSelectIndex + 1, self.ui.list_widget_option.count()):
            self.ui.list_widget_option.item(i).setText(str(i))
        self.ui.list_widget_option.takeItem(nowSelectIndex)

        self.tmp_SelectQuestion.RemoveOption(nowSelectIndex + 1)

    # 獲取題目表
    def LoadQuestionList(self):
        if self.mode == self.MODE_ADD_QUESTION:
            return
        questionLevel = self.question_level  # 搜尋的條件
        self.questionList = self.model.GetQuestionList(questionLevel)
        # 重新添加題目
        self.ui.list_weight_question.clear()
        for i in range(len(self.questionList)):
            q_head = str(self.questionList[i].GetQuestionNumber()) + '. ' + (self.questionList[i].GetQuestion())[:20]
            self.ui.list_weight_question.addItem(q_head)

    # 真正新增題目
    def AddQuestion(self):
        # 新增填充題
        if self.question_mode == self.MODE_FILLING_QUESTION:
            newQuestion = MyLibrary.Question(0, self.ui.text_edit_question.toPlainText())
            self.model.AddFillingQuestion(newQuestion, self.question_level, self.imageList)
        # 新增選擇題
        elif self.question_mode == self.MODE_SELECT_QUESTION:
            self.model.AddSelectQuestion(self.tmp_SelectQuestion, self.question_level)
            #self.model.AddQuestion(newQuestion, self.question_level, self.imageList)
            self.tmp_SelectQuestion = MyLibrary.SelectQuestion(0, "")

        self.ui.text_edit_question.clear()
        self.ui.list_weight_image.clear()
        self.model.CreateQDSLevel()
        self.temp_importImage = None # 清除上一題的圖片
        self.imageList = [] # 清除上一題的圖片
    
    # 儲存題目資訊
    def StoreQuestion(self):
        # 儲存填充題資訊
        if self.editQuestion.GetType() == "FillingQuestion":
            # 處理問題
            nowSelectQuestion = self.editQuestion
            nowSelectQuestion.EditQuestion(self.ui.text_edit_question.toPlainText())
            self.model.EditFillingQuestion(nowSelectQuestion)
            # 處理圖片
            self.model.UpdateDBImageList(self.imageList, nowSelectQuestion.id, nowSelectQuestion.GetType())
            new_item = str(nowSelectQuestion.GetQuestionNumber()) + '. ' + (nowSelectQuestion.GetQuestion())[:20] # 更新list widget item
            self.ui.list_weight_question.currentItem().setText(new_item)
            print("edit")

        # 儲存選擇題資訊
        elif self.editQuestion.GetType() == "SelectQuestion":
            nowEditQuestion = self.tmp_SelectQuestion
            # 再更新的時候已經改了 -> 不用對question Edit
            # 更新資料庫
            self.model.EditSelectQuestion(nowEditQuestion)

            # 更新 list widget
            index = nowEditQuestion.GetQuestionNumber()
            new_item = str(nowEditQuestion.GetQuestionNumber()) + '. ' + (nowEditQuestion.GetQuestion())[:20]
            self.ui.list_weight_question.item(index - 1).setText(new_item)

            # 更新原題目
            self.DeepCopySelectQuestion(self.editQuestion, nowEditQuestion)
            print("edit done")

    # 取得題號
    def GetQuestionIndex(self):
        qList = self.model.GetQuestionList(self.question_level)
        print(qList)
        return len(qList)

    # 格式化圖片
    def FormatImage(self, pixmap):
        pixmap = pixmap.scaled(256, 256, Qt.KeepAspectRatio) # Need from PyQt5.QtCore import Qt
        #if pixmap.size().width() >= pixmap.size().height():
        #    pixmap = pixmap.scaledToWidth(256)
        #else:
        #    pixmap = pixmap.scaledToHeight(256)
        return pixmap

    # 引入圖片
    def ImportImage(self):
        img_path = QFileDialog.getOpenFileName(self, '插入圖片', 'c\\', 'Image files (*.jpg *.png)')
        file_name = img_path[0] #img_path[0] = absolate path of image
        if file_name == "":
            return
        byte_content = MyLibrary.ConvertToBinaryData(file_name) # binary data
        newTempImage = MyLibrary.QDSTempImage(byte_content)
        self.temp_importImage = newTempImage

        pixmap = newTempImage.GetPixmap()
        pixmap = self.FormatImage(pixmap)
        self.ui.label_image_preview.setPixmap(pixmap)
        self.UpdateUI() # 更新UI

    # 新增至圖片列表
    def AddToImageList(self):
        image_id = self.ui.list_weight_image.count() + 1
        self.imageList.append(self.temp_importImage)
        self.ui.list_weight_image.addItem(str(image_id))
        self.temp_importImage = None
        self.ui.label_image_preview.clear() # 清空預覽圖片
        if self.question_mode == self.MODE_SELECT_QUESTION: # 選擇題模式 -> 及時新增
            self.ChangeSelectQuestionImages(self.imageList)
        self.UpdateUI()

    # 刪除圖片
    def DeleteImage(self):
        nowSelectImageIndex = self.ui.list_weight_image.currentRow() # Get Current Row Index
        
        # 沒東東 -> return
        if nowSelectImageIndex == -1:
            return

        # 新增模式中 -> 刪除圖片 
        if self.mode == self.MODE_ADD_QUESTION:
            # 更改後面的圖片的texts
            for i in range(nowSelectImageIndex + 1, self.ui.list_weight_image.count()):
                self.ui.list_weight_image.item(i).setText(str(i))
                
            self.ui.list_weight_image.takeItem(nowSelectImageIndex) # 刪除Item
            self.imageList.pop(nowSelectImageIndex) # 刪除指定索引
            # self.ui.label_image_preview.clear()
        elif self.mode == self.MODE_EDIT_QUESTION:
            image_index = self.GetImageIndex(nowSelectImageIndex)
            select_image = self.imageList[image_index]
            # 圖片存在Server上
            if select_image.IsOnServer:
                select_image.IsUpdated = True
                select_image.IsShowOnListWidget = False
                print("onserver delete")
            # 圖片不存在於Server上
            else:
                self.imageList.pop(image_index)
            self.UpdateImageListWidget()
       
    # 選擇圖片 - 更新預覽圖片
    def SelectImage(self, item):
        nowSelectImageIndex = self.ui.list_weight_image.currentRow() # Get Current Row Index
        print(nowSelectImageIndex)
        # 沒東東 -> return
        if nowSelectImageIndex == -1:
            self.ui.label_image_preview.clear()
            return

        # 編輯模式中 -> 點選圖片 > 預覽圖片
        if self.mode == self.MODE_EDIT_QUESTION:
            # 先取得 所選列對應到image list 對應的 index
            image_index = self.GetImageIndex(nowSelectImageIndex)
            
            select_image = self.imageList[image_index]
            self.ui.label_image_preview.setPixmap(select_image.GetFormatPixmap()) # 設置圖片
       
        # 新增模式中 -> 點選圖片 > 預覽圖片
        if self.mode == self.MODE_ADD_QUESTION:
            qds_temp_image = self.imageList[nowSelectImageIndex]
            self.ui.label_image_preview.setPixmap(qds_temp_image.GetFormatPixmap())

    # 選擇題目 - 更新題目右側資訊
    def SelectQuestion(self, item):
        # nowSlectQuestion = item.text()
        # self.ui.text_edit_question.setPlainText(item.text())

        nowSlectIndex = self.ui.list_weight_question.currentRow()

        # 沒選到就return
        if nowSlectIndex == -1:
            return

        # 編輯模式中 選擇題時出現選擇題的View
        if self.mode == self.MODE_EDIT_QUESTION:
            if self.questionList[nowSlectIndex].GetType() == "SelectQuestion":
                self.ui.label.setVisible(True)
                self.ui.list_widget_option.setVisible(True)
                self.ui.list_widget_option.clear()
                for i in range(4):
                    self.ClickAddOptionButton()
            else:
                self.ui.label.setVisible(False)
                self.ui.list_widget_option.setVisible(False)

        # 新增模式中 且 新增選擇題
        if self.mode == self.MODE_ADD_QUESTION:
            if self.question_mode == self.MODE_SELECT_QUESTION:
                self.ui.list_widget_option.setCurrentRow(-1) # 選項列表取消Focus
                self.select_question_edit_what = "question"

                self.ui.text_edit_question.setPlainText(self.tmp_SelectQuestion.GetQuestion()) # 更新文字框
                self.imageList = self.tmp_SelectQuestion.GetImages()
                self.UpdateImageListWidget()
                return
            
        self.editQuestion = self.questionList[nowSlectIndex]
        # 編輯模式中
        if self.mode == self.MODE_EDIT_QUESTION:
            # 編輯填充題
            if self.editQuestion.GetType() == "FillingQuestion":
                self.tmp_SelectQuestion = None
                self.select_question_edit_what = ""
                self.ui.label_image_preview.clear() # 清空預覽圖片
                self.ui.text_edit_question.setPlainText(self.editQuestion.GetAnswer())

                text = str(self.ui.text_edit_question.toPlainText())
                print(type(text), text)
        
                self.imageList = self.model.GetImagesByQuestion(self.editQuestion)
                self.UpdateImageListWidget()
            # 編輯選擇題
            # editQuestion -> 預編輯的題目, tmpSelectQuestion先複製他出來
            # (讓接下來選選項 換答案的操作 不影響原題目)
            # 如果editQuestion切換其他選擇題 or 換成填充題 放棄tmpSelectQuestion
            elif self.editQuestion.GetType() == "SelectQuestion":
                if self.tmp_SelectQuestion is None or self.tmp_SelectQuestion.id != self.editQuestion.id:
                    self.tmp_SelectQuestion = copy.deepcopy(self.editQuestion)
                self.ui.list_widget_option.setCurrentRow(-1) # 選項列表取消Focus
                self.select_question_edit_what = "question"

                self.ui.text_edit_question.setPlainText(self.tmp_SelectQuestion.GetQuestion()) # 更新文字框
                self.imageList = self.tmp_SelectQuestion.GetImages()
                self.UpdateImageListWidget()
                return

    # 選擇選項 - 選擇題模式中
    def SelectOption(self, item):
        nowSelectIndex = self.ui.list_widget_option.currentRow()
        if nowSelectIndex == -1:
            return

        option = self.tmp_SelectQuestion.GetOption(nowSelectIndex + 1)
        self.ui.list_weight_question.setCurrentRow(-1) # 題目列表取消Focus
        self.select_question_edit_what = str(option.GetNumber())
            
        self.ui.text_edit_question.setPlainText(option.Content) # 更新文字框
        self.imageList = option.GetImages()
        self.UpdateImageListWidget()

    # image list_widget裡面的東西全部更新
    def UpdateImageListWidget(self):
        k = 1
        self.ui.list_weight_image.clear()
        for image in self.imageList:
            if image.IsShowOnListWidget:
                self.ui.list_weight_image.addItem(str(k))
                k += 1

    # 選擇圖片時 取得真正在image List出現的image index
    def GetImageIndex(self, nowSelectImageIndex):
        image_index = 0
        temp_index = 0
        for image in self.imageList:
            if image.IsShowOnListWidget: # 如果他在list widget中
                if temp_index == nowSelectImageIndex: # 而且index = 所選的列
                    break
                else:
                    temp_index += 1
            image_index += 1
        return image_index

    # 接收 來自上一層的題目列表
    def GetQuestionLevelList(self, questionList):
        self.question_level_list = questionList
        self.question_level = self.question_level_list[0]

    # 輸入事件
    def InputTextEdit(self, widget):
        # 新增題目模式
        if self.mode == self.MODE_ADD_QUESTION:
            if self.question_mode == self.MODE_SELECT_QUESTION:
                new_content = widget.toPlainText()
                self.ChangeSelectQuestionContent(new_content)
        # 編輯題目模式
        elif self.mode == self.MODE_EDIT_QUESTION:
            if self.tmp_SelectQuestion is not None:
                new_content = widget.toPlainText()
                self.ChangeSelectQuestionContent(new_content)

    # 改變選擇題 或 其選項的Content
    def ChangeSelectQuestionContent(self, newContent):
        if self.select_question_edit_what == "question":
            self.tmp_SelectQuestion.SetQuestionContent(newContent)
        elif self.select_question_edit_what != "":
            option = self.tmp_SelectQuestion.GetOption(int(self.select_question_edit_what))
            option.SetContent(newContent)

    # 改變選擇題 或 其選項的 images (images = list)
    def ChangeSelectQuestionImages(self, images):
        if self.select_question_edit_what == "question":
            self.tmp_SelectQuestion.SetImages(images)
        elif self.select_question_edit_what != "":
            option = self.tmp_SelectQuestion.GetOption(int(select_question_edit_what))
            option.SetImages(images)

    # 深層複製select question
    def DeepCopySelectQuestion(self, select, copy):
        select.SetQuestionContent(copy.GetQuestion())
        select.answer = copy.GetAnswer()
        select.SetImages(copy.GetImages())
        self.option = copy.option

    def DeepCopySelectOption(self, option, copy):
        option.SetContent(copy.GetContent())
        option.SetImages(copy.GetImages())