import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from view import Make_Question_Page_Test, Add_Edit_Question_Page, Make_Question_Page

# 開啟視窗
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()

    # 出題頁面
    # myMainWindow = Make_Question_Page.MakeQuestionPage()
    myMainWindow = Make_Question_Page_Test.MakeQuestionPage()

    # 新增 / 修改題目頁面
    #myMainWindow = Add_Edit_Question_Page.AddEditQuestionPage()

    myMainWindow.show()
    sys.exit(app.exec_())
