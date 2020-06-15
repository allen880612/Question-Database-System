import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from view import Make_Question_Page_Test, Add_Edit_Question_Page, Make_Question_Page
from model.ExcelModel import ExcelModel


def Show_MakeQuestionPage():
    MakeQuestionPage.show()
    AddEditQuestionPage.hide()
    MakeQuestionPage.comboboxView.CreateDictForLevel()


def Show_AddEditQuestionPage():
    MakeQuestionPage.hide()
    AddEditQuestionPage.show()
    AddEditQuestionPage.comboboxView.CreateDictForLevel()


# 開啟視窗
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MakeQuestionPage = QMainWindow()    

    EXCEL_PATH = "database/盈虧問題v2.xlsx"
    model = ExcelModel(EXCEL_PATH)

    # 出題頁面
    MakeQuestionPage = Make_Question_Page.MakeQuestionPage(model)
    # MakeQuestionPage = Make_Question_Page_Test.(model)

    # 新增 / 修改題目頁面
    AddEditQuestionPage = Add_Edit_Question_Page.AddEditQuestionPage(model)

    MakeQuestionPage.ui.btn_edeit_add.clicked.connect(Show_AddEditQuestionPage)
    AddEditQuestionPage.ui.button_make_question.clicked.connect(Show_MakeQuestionPage)
    Show_MakeQuestionPage()

    sys.exit(app.exec_())
