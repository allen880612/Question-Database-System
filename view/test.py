from PyQt5 import QtCore, QtGui, QtWidgets
from controller import GET_PATH as gp
import os

class Ui_MainWindow(object):
    path = ""
    DATABASE = "database/"
    fManager = gp.FolderManager()
    path2 = ["database/"]
    wordPath = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 571, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setGeometry(QtCore.QRect(160, 300, 75, 23))
        self.btn_confirm.setObjectName("btn_confirm")
        self.cBox_dir1 = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_dir1.setGeometry(QtCore.QRect(60, 200, 121, 21))
        self.cBox_dir1.setObjectName("cBox_dir1")
        self.cBox_dir2 = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_dir2.setGeometry(QtCore.QRect(210, 200, 121, 21))
        self.cBox_dir2.setObjectName("cBox_dir2")
        self.cBox_word = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_word.setGeometry(QtCore.QRect(360, 200, 191, 21))
        self.cBox_word.setObjectName("cBox_word")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 180, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 180, 71, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.InitGUI()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Question Database"))
        self.label.setText(_translate("MainWindow", "請選擇試題範圍"))
        self.btn_confirm.setText(_translate("MainWindow", "確定"))
        self.label_2.setText(_translate("MainWindow", "資料夾 一層"))
        self.label_3.setText(_translate("MainWindow", "資料夾 二層"))
        self.label_4.setText(_translate("MainWindow", "Word"))

    def InitGUI(self):
        # 先放著，之後應該會用到
        fullDir = os.walk(self.DATABASE)
        for fr in fullDir:
            print(fr)

        self.btn_confirm.clicked.connect(self.Confirm)
        self.path = self.DATABASE
        self.cBox_dir1.addItems(self.fManager.GetNextLevel(self.DATABASE))
        self.cBox_dir1.activated[str].connect(self.RebuildDir2)
        self.cBox_dir2.activated[str].connect(self.RebuildDir3)
        self.cBox_word.activated[str].connect(self.GetWordPath)

        self.cBox_dir1.setEditable(True)
        self.cBox_dir2.setEditable(True)
        self.cBox_word.setEditable(True)
        self.cBox_dir1.lineEdit().setText("請選擇科目")
        self.cBox_dir2.lineEdit().setText("請先選擇科目")
        self.cBox_word.lineEdit().setText("請選擇科目及分類")

    def RebuildDir2(self, text):
        dir = []
        print("len 2 = " + str(len(self.path2)))
        self.cBox_dir2.clear()
        # self.path = self.DATABASE
        # self.path = os.path.join(self.path, text)
        # print("dir2 = " + self.path)
        # dir = self.fManager.GetNextLevel(self.path)
        if len(self.path2) < 2:
            self.path2.append(text)
        else:
            self.path2[1] = text
        pd = self.path2[:2]
        print(pd)
        path = os.path.join(*pd)
        print("dir2 = " + path)
        dir = self.fManager.GetNextLevel(path)

        # 判斷路徑是否存在，且為資料夾
        if dir:
            self.cBox_dir2.addItems(dir)
            self.cBox_dir2.setEditText("請選擇科目")
            self.cBox_word.setEditText("請選擇題庫")

    def RebuildDir3(self, text):
        dir = []
        self.cBox_word.clear()
        # finalPath = os.path.join(self.path, text)
        # print("dir3 = " + finalPath)
        # dir = self.fManager.GetNextLevel(finalPath)
        if len(self.path2) < 3:
            self.path2.append(text)
        else:
            self.path2[2] = text
        pd = self.path2[:3]
        print(pd)
        path = os.path.join(*pd)
        print("dir3 = " + path)
        dir = self.fManager.GetNextLevel(path)
        # 判斷路徑是否存在，且為資料夾
        if dir:
            self.cBox_word.addItems(dir)
            self.cBox_word.setEditText("請選擇題庫")

    def GetWordPath(self, text):
        print("Word name : " + text)
        self.label.setText(text)

        if len(self.path2) < 4:
            self.path2.append(text)
        else:
            self.path2[3] = text
        print(self.path2)
        self.wordPath = os.path.join(*self.path2)
        # os.startfile(self.wordPath)
        print("word path = " + self.wordPath)

    def Confirm(self):
        if os.path.isfile(self.wordPath):
            os.startfile(self.wordPath)
            print("open " + self.wordPath)
        else:
            self.label.setText("輸入不完全，或文件已損毀!")







