import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from view import Make_Question_Page_Test, Add_Edit_Question_Page, Make_Question_Page
from view import Select_Question_Page
from model.ExcelModel import ExcelModel

# 開啟出題視窗
def Show_MakeQuestionPage():
    MakeQuestionPage.comboboxView.CreateDictForLevel()
    MakeQuestionPage.GetQuestionLevelList(SelectQuestionPage.checkbox_leaf_level_list) # 把選擇好的題目給Make Question Page
    MakeQuestionPage.ResetPage() # 重設Make Question Page

    MakeQuestionPage.show()
    AddEditQuestionPage.hide()
    SelectQuestionPage.hide()

# 開啟編輯題目視窗
def Show_AddEditQuestionPage():
    MakeQuestionPage.hide()
    AddEditQuestionPage.show()
    SelectQuestionPage.hide()
    AddEditQuestionPage.comboboxView.CreateDictForLevel()

# 開啟選擇題目階層視窗
def Show_SelectQuestionLevelPage():
    MakeQuestionPage.hide()
    AddEditQuestionPage.hide()
    SelectQuestionPage.show()
    SelectQuestionPage.comboboxView.CreateDictForLevel()

# 開啟視窗
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MakeQuestionPage = QMainWindow()

    EXCEL_PATH = "database/盈虧問題v3.xlsx"
    model = ExcelModel(EXCEL_PATH)

    # 出題頁面
    MakeQuestionPage = Make_Question_Page.MakeQuestionPage(model)

    # 新增 / 修改題目頁面
    AddEditQuestionPage = Add_Edit_Question_Page.AddEditQuestionPage(model)

    # 選擇題目階層頁面
    SelectQuestionPage = Select_Question_Page.SelectQuestionPage(model)

    # 註冊事件
    SelectQuestionPage.ui.button_add_question.clicked.connect(Show_AddEditQuestionPage) # 選擇路徑 -> 新增題目
    SelectQuestionPage.ui.button_make_question.clicked.connect(Show_MakeQuestionPage) # 選擇路徑 -> 出題

    MakeQuestionPage.ui.button_return.clicked.connect(Show_SelectQuestionLevelPage) # 出題 -> 選擇路徑
    AddEditQuestionPage.ui.button_make_question.clicked.connect(Show_SelectQuestionLevelPage) # 新增題目 -> 選擇路徑

    #MakeQuestionPage.make_question_signal.connect(SelectQuestionPage.GetQuestionLevelList)

    #Show_MakeQuestionPage()
    #Show_AddEditQuestionPage()
    Show_SelectQuestionLevelPage()

    sys.exit(app.exec_())
