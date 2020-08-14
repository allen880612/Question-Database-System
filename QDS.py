import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from view import Make_Question_Page_Test, Add_Edit_Question_Page, Make_Question_Page
from view import Select_Question_Page
from model.ExcelModel import ExcelModel
import pymysql as mysql
import os
import threading
from model import SQLExtend

# 開啟Proxy
def StartProxy():
    exe_name = "cloud_sql_proxy.exe"
    sql_id = "psyched-circuit-286314:asia-east1:xtest00=tcp:3306"
    key_name = "qds_key.json"
    cmd1 = "-instances=" + sql_id
    cmd2 = "-credential_file=" + key_name
    full_cmd = exe_name + " " + cmd1 + " " + cmd2 + " "
    os.popen("cd proxy" + " && " + full_cmd)

# 開啟出題視窗
def Show_MakeQuestionPage():
    MakeQuestionPage.comboboxView.CreateDictForLevel()
    MakeQuestionPage.GetQuestionLevelList(SelectQuestionPage.GetLeafNodeBySort()) # 把選擇好的題目給Make Question Page
    MakeQuestionPage.ResetPage() # 重設Make Question Page

    MakeQuestionPage.show()
    AddEditQuestionPage.hide()
    SelectQuestionPage.hide()

# 開啟編輯題目視窗
def Show_AddEditQuestionPage():
    AddEditQuestionPage.comboboxView.CreateDictForLevel()
    AddEditQuestionPage.GetQuestionLevelList(SelectQuestionPage.GetLeafNodeBySort())
    AddEditQuestionPage.ResetPage() # 重設 Add Edit Question Page 

    MakeQuestionPage.hide()
    AddEditQuestionPage.show()
    SelectQuestionPage.hide()

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

    #proxy = threading.Thread(target = StartProxy)
    #proxy.start()
    #proxy.join()

    #myDB = mysql.connect(host="35.194.198.56",port=3306,user="user01",passwd="user01",db="QuestionDatabase")
    #model.db = myDB

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
    AddEditQuestionPage.ui.button_return.clicked.connect(Show_SelectQuestionLevelPage) # 新增題目 -> 選擇路徑

    #MakeQuestionPage.make_question_signal.connect(SelectQuestionPage.GetQuestionLevelList)

    #Show_MakeQuestionPage()
    #Show_AddEditQuestionPage()
    Show_SelectQuestionLevelPage()

    sys.exit(app.exec_())
