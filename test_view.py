import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import test, mainwindow as mw

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    myUi = test.Ui_MainWindow()
    myUi.setupUi(myMainWindow)
    myMainWindow.show()
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     myMainWindow = QMainWindow()
#     myUi = mw.Ui_MainWindow()
#     myUi.setupUi(myMainWindow)
#     myMainWindow.show()
#     sys.exit(app.exec_())