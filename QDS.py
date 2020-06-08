import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from view import test, create_edit_question

# 開啟視窗
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    # myUi = test.Ui_MainWindow()
    # myUi.setupUi(myMainWindow)
    myMainWindow = create_edit_question.Craeate_question()

    myMainWindow.show()
    sys.exit(app.exec_())
