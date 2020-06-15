from PyQt5.QtWidgets import QMainWindow
from view import ComboboxView as cbview
from view.UI import Make_Question_UI_Test as mq_UI_Test
from view.UI import Make_Question_UI as mq_UI
from model import MyLibrary
import random
import os
import docx
from functools import partial

class MakeQuestionPage(QMainWindow):

    #region 變數宣告
    TEMPLATE_WORD_PATH = "database/default.docx"
    comboboxSelectOption = []
    #endregion

    def __init__(self, _model):
        super(MakeQuestionPage, self).__init__()

        self.ui = mq_UI.MakeQuestionPage_UI()
        self.ui.setupUi(self)

        self.cBoxList = [self.ui.cBox_level1, self.ui.cBox_level2, self.ui.cBox_level3, self.ui.cBox_level4, self.ui.cBox_level5]
        self.cBoxNum = len(self.cBoxList)
        self.model = _model
        self.comboboxView = cbview.ComboboxView(self.model)
        self.InitGUI()

    #region UI 設定
    def InitGUI(self):

        self.ui.btn_confirm.clicked.connect(self.Confirm)
        #region 下拉式選單
        defaultString = self.comboboxView.GetNoSelectString()
        self.cBoxList[0].addItems(self.comboboxView.GetDictValue(defaultString))

        for i in range(5):
            # self.cBoxList2[i].activated[str].connect(lambda text: self.SelectLevel(i, text))  # 先封印，不知為啥參數總是錯
            self.cBoxList[i].activated[str].connect(partial(self.SelectLevel, i))
            self.cBoxList[i].setEditable(True)
            self.cBoxList[i].lineEdit().setText("選擇第" + str(i + 1) + "層")
        #endregion
    #endregion

    #region 函式區

    def SelectLevel(self, index, text):
        self.UpdateSelectOption(index)      # 更新ComboboxSelectOption = 目前選到的層級 (之後做成key)
        self.UpdateComboBox(index, text)    # 先刪除後面的下拉選單的items再重新加入

    def ClearCombobox(self):
        self.comboboxSelectOption.clear()
        self.cBoxList[0].addItems(self.comboboxView.GetDictValue(self.comboboxView.GetNoSelectString()))  # add default items

        for i in range(1, self.cBoxNum):
            self.cBoxList[i].lineEdit().setText("選擇第" + str(i + 1) + "層")

    def UpdateSelectOption(self, index):
        self.comboboxSelectOption.clear()
        for i in range(index+1):
            self.comboboxSelectOption.append(self.cBoxList[i].currentText())

    def UpdateComboBox(self, index, text):
        # 更新所選文字
        self.cBoxList[index].setEditText(text)

        # 清除所選之後的選擇
        for i in range(self.cBoxNum-1, index):
            self.cBoxList[i].clear()
            self.cBoxList[i].lineEdit().setText("選擇第" + str(i + 1) + "層")

        # 非末項，更新後一選項選擇
        if index != self.cBoxNum - 1:
            self.cBoxList[index + 1].clear()
            self.cBoxList[index + 1].addItems(self.comboboxView.GetDictValue(MyLibrary.CreateDictKey(self.comboboxSelectOption)))
            self.cBoxList[index + 1].lineEdit().setText("選擇第" + str(index + 2) + "層")

    def Confirm(self):

        #excel
        if self.model.IsLoad():
            #questionType = ["數學"]
            questionType = self.comboboxSelectOption #搜尋的條件
            if questionType: #存在搜尋條件才做
                # self.model.GetFilteredDataframe(questionType)
                questionNumber = 10  # 預設隨機選10題
                # qList = self.model.GetQuestionList()  # 取得過濾後的題目
                qList = self.model.GetQuestionList(questionType)  # 取得過濾後的題目
                qList = random.sample(qList, min(questionNumber, len(qList)))  # 將題目不重複隨機選擇 k 題 (0 <= k <= 篩選後的題目數量)
                print(questionType)
                print(qList)
                self.BulidWord(qList, "answer", True)  # 建造word 保留答案
                self.BulidWord(qList, "question", False)  # 建造word 刪除答案
                self.ClearCombobox()  # 清除選擇的combobox
                print("done")
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