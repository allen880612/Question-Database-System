from PyQt5 import QtCore, QtGui, QtWidgets
from controller import GET_PATH as gh
import os

class Ui_MainWindow(object):
    DATABASE = "database/"
    fManager = gh.FolderManager()
    path = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 50, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setGeometry(QtCore.QRect(160, 340, 75, 23))
        self.btn_confirm.setObjectName("btn_confirm")
        self.group_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.group_1.setGeometry(QtCore.QRect(60, 130, 120, 80))
        self.group_1.setObjectName("group_1")
        self.rb_basic = QtWidgets.QRadioButton(self.group_1)
        self.rb_basic.setGeometry(QtCore.QRect(10, 20, 83, 16))
        self.rb_basic.setCheckable(True)
        self.rb_basic.setChecked(False)
        self.rb_basic.setObjectName("rb_basic")
        self.rb_select = QtWidgets.QRadioButton(self.group_1)
        self.rb_select.setGeometry(QtCore.QRect(10, 50, 83, 16))
        self.rb_select.setObjectName("rb_select")
        self.group_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.group_2.setGeometry(QtCore.QRect(210, 130, 120, 80))
        self.group_2.setObjectName("group_2")
        self.rb_first = QtWidgets.QRadioButton(self.group_2)
        self.rb_first.setGeometry(QtCore.QRect(10, 20, 83, 16))
        self.rb_first.setCheckable(True)
        self.rb_first.setChecked(False)
        self.rb_first.setObjectName("rb_first")
        self.rb_second = QtWidgets.QRadioButton(self.group_2)
        self.rb_second.setGeometry(QtCore.QRect(10, 50, 83, 16))
        self.rb_second.setObjectName("rb_second")
        self.cBox_dir1 = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_dir1.setGeometry(QtCore.QRect(60, 250, 121, 21))
        self.cBox_dir1.setObjectName("cBox_dir1")
        self.cBox_dir2 = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_dir2.setGeometry(QtCore.QRect(210, 250, 121, 21))
        self.cBox_dir2.setObjectName("cBox_dir2")
        self.cBox_word = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_word.setGeometry(QtCore.QRect(360, 250, 191, 21))
        self.cBox_word.setObjectName("cBox_word")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 230, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 230, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 230, 71, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "選我啊"))
        self.btn_confirm.setText(_translate("MainWindow", "確定"))
        self.group_1.setTitle(_translate("MainWindow", "科目"))
        self.rb_basic.setText(_translate("MainWindow", "基礎化學"))
        self.rb_select.setText(_translate("MainWindow", "選修化學"))
        self.group_2.setTitle(_translate("MainWindow", "年度"))
        self.rb_first.setText(_translate("MainWindow", "上"))
        self.rb_second.setText(_translate("MainWindow", "下"))
        self.label_2.setText(_translate("MainWindow", "科目"))
        self.label_3.setText(_translate("MainWindow", "分類"))
        self.label_4.setText(_translate("MainWindow", "題庫"))

    def InitGUI(self):
        # 先放著，之後應該會用到
        fullDir = os.walk(self.DATABASE)
        for fr in fullDir:
            print(fr)

        self.path = self.DATABASE
        self.cBox_dir1.addItems(self.fManager.GetNextLevel(self.DATABASE))
        self.cBox_dir1.activated[str].connect(self.RebuildDir2)
        self.cBox_dir2.activated[str].connect(self.RebuildDir3)
        self.cBox_word.activated[str].connect(self.GetWordPath)

        self.cBox_dir1.setEditable(True)
        self.cBox_dir1.lineEdit().setText("請選擇科目")
        self.cBox_dir2.setEditable(True)
        self.cBox_dir2.lineEdit().setText("請先選擇科目")
        self.cBox_word.setEditable(True)
        self.cBox_word.lineEdit().setText("請選擇科目及分類")

    def RebuildDir2(self, text):
        dir = []
        self.cBox_dir2.clear()
        self.path = self.DATABASE
        self.path = os.path.join(self.path, text)
        print(self.path)
        print("dir2 = " + self.path)
        dir = self.fManager.GetNextLevel(self.path)
        # 判斷路徑是否存在，且為資料夾
        if dir:
            self.cBox_dir2.addItems(dir)

    def RebuildDir3(self, text):
        dir = []
        self.cBox_word.clear()
        finalPath = os.path.join(self.path, text)
        print("dir3 = " + finalPath)
        dir = self.fManager.GetNextLevel(finalPath)
        # 判斷路徑是否存在，且為資料夾
        if dir:
            self.cBox_word.addItems(dir)

    def GetWordPath(self, text):
        print("Word name : " + text)
        self.label.setText(text)





