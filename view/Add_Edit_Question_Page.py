from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from model import MyLibrary
from view.UI import Add_Edit_Question_UI
from view import ComboboxView as cbView
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
        self.comboboxView = cbView.ComboboxView(self.model)
        self.cBoxList = [self.ui.cBox_lv1, self.ui.cBox_lv2, self.ui.cBox_lv3, self.ui.cBox_lv4, self.ui.cBox_lv5]
        self.cBoxNum = len(self.cBoxList)

        #region 新增單元 視窗 變數 (移到主畫面)
        #self.Add_Unit_View = Add_Unit_Page.AddUnitPage(self.model)
        #self.Add_Unit_View.setWindowModality(Qt.ApplicationModal)
        #endregion

        self.Initialize()

    # 初始化
    def Initialize(self):
        self.ConnectEvent()
        self.LoadComboBox()
        self.InitUI()
        self.UpdateUI()
        self.mode = self.MODE_ADD_QUESTION

    # 註冊事件
    def ConnectEvent(self):
        self.ui.button_add_question.clicked.connect(self.ClickAddQuestionButton)
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

    # 初始化UI
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
        # flag = flag and (not len(self.ui.text_edit_question.toPlainText()) == 0)
        # print(f"cBox={len(self.comboboxSelectOption) == self.cBoxNum}")
        flag = flag and (len(self.comboboxSelectOption) == self.cBoxNum)
        print(f"flag={flag}")
        return flag

    # 更新UI
    def UpdateUI(self):
        # 空白題目 不該被新增 /修改
        self.ui.button_add_question.setEnabled(self.GetAddButtonEnable())
        # 未選擇單元 不該能修改
        self.ui.button_edit_question_mode.setEnabled(self.GetEditButtonEnable())
        # 未引入圖片 不能新增
        self.ui.button_addToList_image.setEnabled(self.temp_importImage != "")

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
        self.ui.label_image_preview.clear() # 清空預覽圖片

    # 切換至新增模式
    def ClickAddMode(self):
        self.ui.button_edit_question_mode.setEnabled(True)
        self.ui.button_add_question_mode.setEnabled(False)
        self.mode = self.MODE_ADD_QUESTION
        self.ui.text_edit_question.clear()
        self.ui.list_weight_image.clear()
        self.ui.list_weight_question.clear()
        self.ui.label_image_preview.clear() # 清空預覽圖片

    # 點擊 新增題目 按鈕
    def ClickAddQuestionButton(self):
        if self.mode == self.MODE_ADD_QUESTION:
            self.CreateQuestion()

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
            if self.questionList[i].GetQuestionNumber() != 0:
                q_head = str(i) + '. ' + (self.questionList[i].GetQuestion())[:20]
                self.ui.list_weight_question.addItem(q_head)
        # self.ui.list_weight_question.addItems(self.questionList)

    # 真正新增題目
    def AddQuestion(self, dict_q):
        self.model.AddQuestion(dict_q)
        self.ui.text_edit_question.clear()
        self.ui.list_weight_image.clear()
        self.comboboxView.CreateDictForLevel()
        self.temp_importImage = "" # 清除上一提的圖片
        self.imageListPath = [] # 清除上一提的圖片

    # 獲取題目資訊，建立題目類別
    def CreateQuestion(self):
        questionList = self.model.GetQuestionList(self.comboboxSelectOption)
        newQuestionIndex = len(questionList)
        q_info = copy.deepcopy(self.comboboxSelectOption)
        q_info.append(newQuestionIndex)
        q_info.append(self.ui.text_edit_question.toPlainText())
        q_info.append(self.GetImageIndex(str(newQuestionIndex))) # 新增&加入圖片

        # 只有一題寫那題是0 -> 編輯問題
        if len(questionList) == 1 and questionList[0].GetQuestionNumber() == 0:
            self.model.EditQuestion(0, q_info)
        else: # 有很多題 -> 新增問題
            # list = ['數學', '應用題', '典型應用題', '燕尾定理', '胖子', 2, '操你媽', 'NOIMAGE']
            dict_q = dict(zip(self.model.GetOriginalDataFrame().columns, q_info))
            # print(dict_q)
            self.AddQuestion(dict_q)

    # 取得題號
    def GetQuestionIndex(self):
        qList = self.model.GetQuestionList(self.comboboxSelectOption)
        print(qList)
        return len(qList)

    # 格式化圖片
    def FormatImage(self, pixmap):
        # pixmap = pixmap.scaled(256, 256, Qt.KeepAspectRatio) # Need from PyQt5.QtCore import Qt
        if pixmap.size().width() >= pixmap.size().height():
            pixmap = pixmap.scaledToWidth(256)
        else:
            pixmap = pixmap.scaledToHeight(256)
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
        for dir in self.comboboxSelectOption:
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
            dir_path = MyLibrary.GetFolderPathByList(self.comboboxSelectOption)
            image_name = item.text()
            dir_path = os.path.join(dir_path, image_name)
            self.ui.label_image_preview.setPixmap(QPixmap(dir_path)) # 設置圖片
       
        # 新增模式中 -> 點選圖片 > 預覽圖片
        if self.mode == self.MODE_ADD_QUESTION:
            image_path = self.imageListPath[nowSelectImageIndex]
            self.ui.label_image_preview.setPixmap(QPixmap(image_path))


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

    ## 開啟 新增單元 視窗
    #def OpenAddUnitView(self):
    #    if self.Is_add_unit_view_open == False:
    #        self.Is_add_unit_view_open = True
    #        self.Add_Unit_View.show()
    #        self.Add_Unit_View.ResetPage()

    ## 接收 Add Unit View 的資料 函數 (有幾個參數就接幾個) (bool, list)
    #def GetADdUnitViewData(self, is_close, list_input_content):
    #    if is_close == True:
    #        self.Is_add_unit_view_open = False

    #        if list_input_content != []:
    #            q_Info = copy.deepcopy(list_input_content)
    #            q_Info.append(0) # add 題號
    #            q_Info.append("default Content") # add 內容
    #            q_Info.append("NOIMAGE") # add 圖片
    #            dict_q = dict(zip(self.model.GetOriginalDataFrame().columns, q_Info))
    #            self.model.AddQuestion(dict_q)
    #            self.comboboxView.CreateDictForLevel()