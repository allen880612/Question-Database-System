import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from view import Make_Question_Page_Test, Add_Edit_Question_Page, Make_Question_Page
from view import Select_Question_Page, Select_Subject_Page
from model.ExcelModel import ExcelModel
from model.DBModel import DBModel
import pymysql as mysql
import os
import threading
from model import SQLExtend

# 開啟出題視窗
def Show_MakeQuestionPage():
    MakeQuestionPage.GetQuestionLevelList(SelectQuestionPage.GetLeafNodeBySort()) # 把選擇好的題目給Make Question Page
    MakeQuestionPage.ResetPage() # 重設Make Question Page

    MakeQuestionPage.show()
    AddEditQuestionPage.hide()
    SelectQuestionPage.hide()
    SelectSubjectPage.hide()

# 開啟編輯題目視窗
def Show_AddEditQuestionPage():
    AddEditQuestionPage.GetQuestionLevelList(SelectQuestionPage.GetLeafNodeBySort())
    AddEditQuestionPage.ResetPage() # 重設 Add Edit Question Page 

    MakeQuestionPage.hide()
    AddEditQuestionPage.show()
    SelectQuestionPage.hide()
    SelectSubjectPage.hide()

# 開啟選擇題目階層視窗
def Show_SelectQuestionLevelPage():
    SelectQuestionPage.SetSelectSubject(SelectSubjectPage.GetSelectSubject())
    SelectQuestionPage.ResetPage()

    MakeQuestionPage.hide()
    AddEditQuestionPage.hide()
    SelectQuestionPage.show()
    SelectSubjectPage.hide()

# 開啟選擇科目頁面
def Show_SelectSubjectPage():
    MakeQuestionPage.hide()
    AddEditQuestionPage.hide()
    SelectQuestionPage.hide()
    SelectSubjectPage.show()

# 開啟視窗
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MakeQuestionPage = QMainWindow()

    model = DBModel()

    # 出題頁面
    MakeQuestionPage = Make_Question_Page.MakeQuestionPage(model)

    # 新增 / 修改題目頁面
    AddEditQuestionPage = Add_Edit_Question_Page.AddEditQuestionPage(model)

    # 選擇題目階層頁面
    SelectQuestionPage = Select_Question_Page.SelectQuestionPage(model)

    # 選擇單元頁面
    SelectSubjectPage = Select_Subject_Page.SelectSubjectPage(model)

    # 註冊事件
    SelectQuestionPage.ui.button_add_question.clicked.connect(Show_AddEditQuestionPage) # 選擇路徑 -> 新增題目
    SelectQuestionPage.ui.button_make_question.clicked.connect(Show_MakeQuestionPage) # 選擇路徑 -> 出題

    MakeQuestionPage.ui.button_return.clicked.connect(Show_SelectQuestionLevelPage) # 出題 -> 選擇路徑
    AddEditQuestionPage.ui.button_return.clicked.connect(Show_SelectQuestionLevelPage) # 新增題目 -> 選擇路徑

    SelectSubjectPage.ui.button_confirm.clicked.connect(Show_SelectQuestionLevelPage) # 選擇題目 -> 繼續選擇階層
    #MakeQuestionPage.make_question_signal.connect(SelectQuestionPage.GetQuestionLevelList)

    #Show_MakeQuestionPage()
    #Show_AddEditQuestionPage()
    #Show_SelectQuestionLevelPage()
    Show_SelectSubjectPage()

    sys.exit(app.exec_())
