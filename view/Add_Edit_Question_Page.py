from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from model import MyLibrary
from view.UI import Add_Edit_Question_UI
from view import Add_Unit_Page
import pathlib
import copy
import os
import shutil #複製圖片用

class AddEditQuestionPage(QMainWindow):

    comboboxSelectOption = []
    questionList = []
    imageListPath = []
    temp_importImage = ""
    MODE_ADD_QUESTION = "add_question"
    MODE_EDIT_QUESTION = "edit_question"
    mode = ""
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
        self.ui.text_edit_question.textChanged.connect(self.UpdateUI)
        self.ui.button_edit_question_mode.clicked.connect(self.ClickEditMode)
        self.ui.button_add_question_mode.clicked.connect(self.ClickAddMode)
        self.ui.list_weight_image.currentItemChanged.connect(self.SelectImage) # 選擇圖片
        
        # 新增單元 視窗 (移到選擇路徑畫面)
        # self.ui.button_add_unit.clicked.connect(self.OpenAddUnitView)
        # self.Add_Unit_View.add_unit_signal.connect(self.GetADdUnitViewData)

    # 重設頁面
    def ResetPage(self):
        defaultString = self.model.DefaultString_NoSelect
        self.ClickAddMode()
        self.ui.label_question_level.setText(MyLibrary.GetQuestionShowText(self.question_level))
        self.mode = self.MODE_ADD_QUESTION

    # 新增按鈕是否可以按下
    def GetAddQuestionButtonEnable(self):
        #flag = True
        ## print(f"text={not len(self.ui.text_edit_question.toPlainText()) == 0}")
        #flag &= (not len(self.ui.text_edit_question.toPlainText()) == 0)
        ## print(f"cBox={len(self.comboboxSelectOption) == self.cBoxNum}")
        #flag &= (len(self.comboboxSelectOption) == 0)
        ## print(f"flag={flag}")
        #return flag
        return len(self.ui.text_edit_question.toPlainText()) != 0

    # 編輯按鈕是否可以按下
    def GetEditButtonEnable(self):
        #flag = True
        # print(f"text={not len(self.ui.text_edit_question.toPlainText()) == 0}")
        # flag = flag and (not len(self.ui.text_edit_question.toPlainText()) == 0)
        # print(f"cBox={len(self.comboboxSelectOption) == self.cBoxNum}")
        #flag = flag and (len(self.comboboxSelectOption) == self.cBoxNum)
        #print(f"flag={flag}")
        #return flag 
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
        self.ui.button_addToList_image.setEnabled(self.temp_importImage != "")

        # 切換模式按鈕
        self.ui.button_add_question_mode.setEnabled(self.IsAddModeButtonEnable())
        self.ui.button_edit_question_mode.setEnabled(self.IsEditModeButtonEnable())

    # 切換至編輯模式
    def ClickEditMode(self):
        self.mode = self.MODE_EDIT_QUESTION
        self.ui.list_weight_image.clear()
        self.LoadQuestionList()
        self.ui.label_image_preview.clear() # 清空預覽圖片
        self.ui.button_add_question.setText("儲存題目")
        self.UpdateUI()

    # 切換至新增模式
    def ClickAddMode(self):
        self.mode = self.MODE_ADD_QUESTION
        self.ui.text_edit_question.clear()
        self.ui.list_weight_image.clear()
        self.ui.list_weight_question.clear()
        self.LoadQuestionList()
        self.ui.label_image_preview.clear() # 清空預覽圖片
        self.ui.button_add_question.setText("新增題目")
        self.UpdateUI()

    # 點擊 新增題目 按鈕
    def ClickAddQuestionButton(self):
        if self.mode == self.MODE_ADD_QUESTION:
            self.CreateQuestion()
        elif self.mode == self.MODE_EDIT_QUESTION:
            self.StoreQuestion()

    # 獲取題目表
    def LoadQuestionList(self):
        if self.mode == self.MODE_ADD_QUESTION:
            return
        #if self.question_level == []:
        #    return
        questionType = self.question_level  # 搜尋的條件
        self.questionList = self.model.GetQuestionList(questionType)
        self.ui.list_weight_question.clear()
        for i in range(len(self.questionList)):
            if self.questionList[i].GetQuestionNumber() != 0:
                q_head = str(self.questionList[i].GetQuestionNumber()) + '. ' + (self.questionList[i].GetQuestion())[:20]
                self.ui.list_weight_question.addItem(q_head)
        # self.ui.list_weight_question.addItems(self.questionList)

    # 真正新增題目
    def AddQuestion(self, dict_q):
        self.model.AddQuestion(dict_q)
        self.ui.text_edit_question.clear()
        self.ui.list_weight_image.clear()
        self.model.CreateQDSLevel()
        self.temp_importImage = "" # 清除上一題的圖片
        self.imageListPath = [] # 清除上一題的圖片

    # 獲取題目資訊，建立題目類別
    def CreateQuestion(self):
        questionList = self.model.GetQuestionList(self.question_level)
        newQuestionIndex = len(questionList)
        q_info = copy.deepcopy(self.question_level)
        q_info.append("") # Level 3
        q_info.append("") # Level 4
        q_info.append("") # Level 5
        q_info.append(newQuestionIndex)
        q_info.append(self.ui.text_edit_question.toPlainText())
        q_info.append(self.GetImageIndex(str(newQuestionIndex))) # 新增&加入圖片
        q_info.append(self.model.GetQuestionCount() - 1)

        # 只有一題且那題是0 -> 編輯問題
        if len(questionList) == 1 and questionList[0].GetQuestionNumber() == 0:
            self.model.EditQuestion(q_info)
        else: # 有很多題 -> 新增問題
            # list = ['數學', '應用題', '典型應用題', '燕尾定理', '胖子', 2, '操你媽', 'NOIMAGE']
            dict_q = dict(zip(self.model.GetOriginalDataFrame().columns, q_info))
            # print(dict_q)
            self.AddQuestion(dict_q)
    
    # 儲存題目資訊
    def StoreQuestion(self):
        nowSelectIndex = self.ui.list_weight_question.currentRow()
        nowSelectQuestion = self.questionList[nowSelectIndex]
        nowSelectQuestion.EditQuestion(self.ui.text_edit_question.toPlainText(), self.GetImageIndex(str(nowSelectQuestion.GetQuestionNumber())))
        q_info = nowSelectQuestion.ConvertToList(self.question_level)
        print("on edit question, q_info: ")
        print(q_info)
        self.model.EditQuestion(q_info, index=nowSelectQuestion.dataframe_index)
        new_item = str(nowSelectQuestion.GetQuestionNumber()) + '. ' + (nowSelectQuestion.GetQuestion())[:20] # 更新list widget item
        self.ui.list_weight_question.currentItem().setText(new_item)

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
        pixmap = QPixmap(file_name)
        pixmap = self.FormatImage(pixmap)
        self.ui.label_image_preview.setPixmap(QPixmap(pixmap))
        self.temp_importImage = file_name
        self.UpdateUI() # 更新UI

    # 新增至圖片列表
    def AddToImageList(self):
        image_id = self.ui.list_weight_image.count() + 1
        self.imageListPath.append(self.temp_importImage)
        self.ui.list_weight_image.addItem(str(image_id))
        self.temp_importImage = ""
        self.ui.label_image_preview.clear() # 清空預覽圖片
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
            self.imageListPath.pop(nowSelectImageIndex) # 刪除指定索引
            # self.ui.label_image_preview.clear()

    # 取得圖片 題號 + 編號
    def GetImageIndex(self, question_index):
        # imageListPath 為空 -> 沒圖片
        if self.imageListPath == []:
            return "NOIMAGE"

        # 創建儲存圖片用資料夾
        dir_path = "database"
        for dir in self.question_level:
            dir_path = os.path.join(dir_path, dir)
        print("new path: " + dir_path)
        if not os.path.exists(dir_path): # 如果資料夾不存在 才建立資料夾
            os.makedirs(dir_path)

        # 搬運圖片至資料夾 & 製造回傳字串
        str_image_index = ""
        for i in range(len(self.imageListPath)):
            file_extensionName = os.path.splitext(self.imageListPath[i])[-1] # 取得副檔名
            newFileName = "" # 製造新檔名 (題號_圖片編號.副檔名)
            if len(self.imageListPath) == 1:
                newFileName = question_index + file_extensionName # 題號.副檔名
            else:
                newFileName = question_index + "_" + str(i + 1) + file_extensionName # 題號_圖片編號.副檔名
            shutil.copy(self.imageListPath[i], os.path.join(dir_path, newFileName)) # 搬運圖片
            str_image_index += newFileName # 製造回傳字串
            if i + 1 < len(self.imageListPath):
                str_image_index += " "

        return str_image_index
       
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
            dir_path = MyLibrary.GetFolderPathByList(self.question_level)
            image_name = item.text()
            dir_path = os.path.join(dir_path, image_name)
            pixmap = QPixmap(dir_path)
            pixmap = self.FormatImage(pixmap)
            self.ui.label_image_preview.setPixmap(pixmap) # 設置圖片
       
        # 新增模式中 -> 點選圖片 > 預覽圖片
        if self.mode == self.MODE_ADD_QUESTION:
            image_path = self.imageListPath[nowSelectImageIndex]
            pixmap = QPixmap(image_path)
            self.FormatImage(pixmap)
            self.ui.label_image_preview.setPixmap(pixmap)


    # 選擇題目 - 更新題目右側資訊
    def SelectQuestion(self, item):
        # nowSlectQuestion = item.text()
        # self.ui.text_edit_question.setPlainText(item.text())

        nowSlectIndex = self.ui.list_weight_question.currentRow()
        # print(nowSlectIndex, type(nowSlectIndex))
        if self.mode == self.MODE_ADD_QUESTION or nowSlectIndex == -1:
            return

        nowSlectQuestion = self.questionList[nowSlectIndex]
        self.ui.label_image_preview.clear() # 清空預覽圖片
        self.ui.text_edit_question.setPlainText(nowSlectQuestion.GetQuestionAnswer())

        text = str(self.ui.text_edit_question.toPlainText())
        print(type(text), text)

        self.ui.list_weight_image.clear()
        path = nowSlectQuestion.GetImage()

        if path:
            for p in path:
                img_name = pathlib.PurePath(p).name
                self.ui.list_weight_image.addItem(img_name)
    
    # 接收 來自上一層的題目列表
    def GetQuestionLevelList(self, questionList):
        self.question_level_list = questionList
        self.question_level = self.question_level_list[0]