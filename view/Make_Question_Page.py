from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from controller import GET_PATH as gp
from view import ComboboxView as cbview
from view.UI import Make_Question_UI as mq_UI
from model import MyLibrary, ExcelModel
import random
import os
import docx


class MakeQuestionPage(QMainWindow):

    #region 變數宣告
    path = ""
    DATABASE = "database/"
    fManager = gp.FolderManager()
    path2 = ["database/"]
    wordPath = ""
    TEMPLATE_WORD_PATH = "database/default.docx"
    #endregion

    def __init__(self):
        super(MakeQuestionPage, self).__init__()

        self.ui = mq_UI.MakeQuestionPage_UI()
        self.ui.setupUi(self)
        self.InitGUI()

    #region Excel
    excelPath = "database/盈虧問題v2.xlsx"
    model = ExcelModel.ExcelModel(excelPath)
    #endregion

    #region 創建下拉式選單
    comboboxView = cbview.ComboboxManager(model.GetOriginalDataFrame())
    comboboxSelectOption = []
    #endregion

    #region UI 設定
    def InitGUI(self):
        # 先放著，之後應該會用到
        fullDir = os.walk(self.DATABASE)
        for fr in fullDir:
            print(fr)

        self.ui.btn_confirm.clicked.connect(self.Confirm)

        #region 下拉式選單
        defaultString = self.comboboxView.GetNoSelectString()
        self.ui.cBox_level1.addItems(self.comboboxView.GetDictValue(defaultString))
        self.ui.cBox_level1.activated[str].connect(self.SelectLevel1)
        self.ui.cBox_level2.activated[str].connect(self.SelectLevel2)
        self.ui.cBox_level3.activated[str].connect(self.SelectLevel3)
        self.ui.cBox_level4.activated[str].connect(self.SelectLevel4)
        self.ui.cBox_level5.activated[str].connect(self.SelectLevel5)


        self.ui.cBox_level1.setEditable(True)
        self.ui.cBox_level2.setEditable(True)
        self.ui.cBox_level3.setEditable(True)
        self.ui.cBox_level4.setEditable(True)
        self.ui.cBox_level5.setEditable(True)

        self.ui.cBox_level1.lineEdit().setText("選擇第一層")
        self.ui.cBox_level2.lineEdit().setText("選擇第二層")
        self.ui.cBox_level3.lineEdit().setText("選擇第三層")
        self.ui.cBox_level4.lineEdit().setText("選擇第四層")
        self.ui.cBox_level5.lineEdit().setText("選擇第五層")
        #endregion
    #endregion

    #region 函式區
    def SelectLevel1(self, text):
        #comboboxSelectOption = 目前選到的層級 (之後做成key)
        self.comboboxSelectOption = [self.ui.cBox_level1.currentText()]
        #先刪除後面的下拉選單的items再重新加入
        self.ui.cBox_level2.clear()
        self.ui.cBox_level3.clear()
        self.ui.cBox_level4.clear()
        self.ui.cBox_level5.clear()
        self.ui.cBox_level2.addItems(self.comboboxView.GetDictValue(text))
        self.ui.cBox_level2.setEditText("選擇第二層")
        self.ui.cBox_level3.setEditText("選擇第三層")
        self.ui.cBox_level4.setEditText("選擇第四層")
        self.ui.cBox_level5.setEditText("選擇第五層")

    def SelectLevel2(self, text):
        self.comboboxSelectOption = [self.ui.cBox_level1.currentText(), self.ui.cBox_level2.currentText()]

        self.ui.cBox_level3.clear()
        self.ui.cBox_level4.clear()
        self.ui.cBox_level5.clear()
        self.ui.cBox_level3.addItems(self.comboboxView.GetDictValue(MyLibrary.CreateDictKey(self.comboboxSelectOption)))
        self.ui.cBox_level3.setEditText("選擇第三層")
        self.ui.cBox_level4.setEditText("選擇第四層")
        self.ui.cBox_level5.setEditText("選擇第五層")

    def SelectLevel3(self, text):
        self.comboboxSelectOption = [self.ui.cBox_level1.currentText(), self.ui.cBox_level2.currentText(), self.ui.cBox_level3.currentText()]

        self.ui.cBox_level4.clear()
        self.ui.cBox_level5.clear()
        self.ui.cBox_level4.addItems(self.comboboxView.GetDictValue(MyLibrary.CreateDictKey(self.comboboxSelectOption)))
        self.ui.cBox_level4.setEditText("選擇第四層")
        self.ui.cBox_level5.setEditText("選擇第五層")

    def SelectLevel4(self, text):
        self.comboboxSelectOption = [self.ui.cBox_level1.currentText(), self.ui.cBox_level2.currentText(), self.ui.cBox_level3.currentText(), self.ui.cBox_level4.currentText()]

        self.ui.cBox_level5.clear()
        self.ui.cBox_level5.addItems(self.comboboxView.GetDictValue(MyLibrary.CreateDictKey(self.comboboxSelectOption)))
        self.ui.cBox_level5.setEditText("選擇第五層")

    def SelectLevel5(self, text):
        self.comboboxSelectOption = [self.ui.cBox_level1.currentText(), self.ui.cBox_level2.currentText(), self.ui.cBox_level3.currentText(), self.ui.cBox_level4.currentText(), self.ui.cBox_level5.currentText()]
        print(self.comboboxSelectOption)

    def ClearCombobox(self):
        self.comboboxSelectOption.clear()
        self.ui.cBox_level1.clear()
        self.ui.cBox_level2.clear()
        self.ui.cBox_level3.clear()
        self.ui.cBox_level4.clear()
        self.ui.cBox_level5.clear()

        self.ui.cBox_level1.addItems(self.comboboxView.GetDictValue(self.comboboxView.GetNoSelectString())) # add default items
        self.ui.cBox_level1.lineEdit().setText("選擇第一層")
        self.ui.cBox_level2.lineEdit().setText("選擇第二層")
        self.ui.cBox_level3.lineEdit().setText("選擇第三層")
        self.ui.cBox_level4.lineEdit().setText("選擇第四層")
        self.ui.cBox_level5.lineEdit().setText("選擇第五層")

    def Confirm(self):

        #excel
        if self.model.IsLoad():
            #questionType = ["數學"]
            questionType = self.comboboxSelectOption #搜尋的條件
            if questionType: #存在搜尋條件才做
                self.model.GetFilteredDataframe(questionType)
                questionNumber = 10  # 預設隨機選10題
                qList = self.model.GetQuestionList()  # 取得過濾後的題目
                qList = random.sample(qList, min(questionNumber, len(qList)))  # 將題目不重複隨機選擇 k 題 (0 <= k <= 篩選後的題目數量)
                print(questionType)
                print(qList)
                self.BulidWord(qList, "answer", True)  # 建造word 保留答案
                self.BulidWord(qList, "question", False)  # 建造word 刪除答案
                self.ClearCombobox()  # 清除選擇的combobox
                print("done")
                # self.excel.GetFilteredDataframe(questionType)
                # questionNumber = 10 #預設隨機選10題
                # questionAnswerList = self.excel.GetQuestionList() #取得過濾後的題目
                # # questionAnswerList = self.excel.GetFilteredQuestion() #取得過濾後的題目
                # questionAnswerList = random.sample(questionAnswerList, min(questionNumber, len(questionAnswerList))) # 將題目不重複隨機選擇 k 題 (0 <= k <= 篩選後的題目數量)
                # questionList = self.DeleteAnswer(questionAnswerList) #刪除答案(【*】)
                # print(questionType)
                # print(questionAnswerList)
                # print(questionList)
                # self.BulidWord(questionAnswerList, "answer") #建造word
                # self.BulidWord(questionList, "question")  # 建造word
                # self.ClearCombobox() #清除選擇的combobox
                # print("done")
            else:
                self.ui.label.setText("未選擇條件")
        #excel

    def BulidWord(self, qList, fileName, haveAnswer):
        word = docx.Document(docx=self.TEMPLATE_WORD_PATH)  # 另一個坑，為了讓方裝後也能抓到default.docx，必須指定
        heading = " - ".join(self.comboboxSelectOption)
        word.add_heading(heading, 0) #新增那個醜醜藍字

        #新增題目 style
        questionStyle = word.styles.add_style("question", docx.enum.style.WD_STYLE_TYPE.PARAGRAPH) #新增一樣式 (樣式名稱, 樣式類型)
        questionStyle.font.size = docx.shared.Pt(12) #更改此樣式的文字大小
        questionStyle.font.name = "Times New Roman" #設定英文字體
        # where am I? who am I???
        questionStyle._element.rPr.rFonts.set(docx.oxml.ns.qn("w:eastAsia"), "細明體") #設定中文字體
        # 設定凸排, su go i ne, my Python
        questionStyle.paragraph_format.first_line_indent = docx.shared.Pt(-18) # 設定首縮排/凸排 (正值 = 縮排, 負值 = 凸排)
        questionStyle.paragraph_format.left_indent = docx.shared.Pt(18) # ↓注意，重點來了，設定"整個段落"縮排  (正常來說應該不用設定，但是設定凸排的時候，他會順便把整個段落也往左移動，所以要他媽的移回來)

        #imageList = self.excel.GetFilteredImage(self.comboboxSelectOption)
        #新增題目
        for i in range(0, len(qList)):
            questionIndex = "(" + str(i + 1) + ") " #題號
            if haveAnswer:
                question = qList[i].GetQuestionAnswer()
            else:
                question = qList[i].GetQuestion()
            paragraph = word.add_paragraph(questionIndex + question, style = "question")
            #paragraph = word.add_paragraph(questionIndex + questionList[i], style = "question") #題號 + 題目 一題作為一個段落
            paragraph.alignment = 0 #設定段落對齊 0 = 靠左, 1 = 置中, 2 = 靠右, 3 = 左右對齊 (WD_PARAGRAPH_ALIGNMENT)
            try:
                # print("have", qList[i].HaveImage())
                # print("image", qList[i].GetImage())
                if qList[i].HaveImage() and qList[i].GetImage():
                    print(qList[i].GetImage())
                    #run = word.paragraphs[i + 1].add_run()
                    imageParagraph = word.add_paragraph() # 為了讓圖片靠右，直接新增一個段落，方便用alignment
                    imageParagraph.alignment = 2
                    run = imageParagraph.add_run()
                    #run.add_break() #不換段換行
                    for image in qList[i].GetImage():
                        run.add_picture(image, height=docx.shared.Cm(2.6))
            except:
                print("Insert image fail!")

        savePath = "word/" + fileName + ".docx"
        word.save(savePath) #存檔 (存在word資料夾)
    #endregion