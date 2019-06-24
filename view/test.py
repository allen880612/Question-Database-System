from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('../controller')
sys.path.append('../model')
from controller import GET_PATH
from model import FetchData
import os

class Ui_MainWindow(object):
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
        self.btn_confirm.setGeometry(QtCore.QRect(180, 260, 75, 23))
        self.btn_confirm.setObjectName("btn_confirm")
        self.group_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.group_1.setGeometry(QtCore.QRect(90, 140, 120, 80))
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
        self.group_2.setGeometry(QtCore.QRect(240, 140, 120, 80))
        self.group_2.setObjectName("group_2")
        self.rb_first = QtWidgets.QRadioButton(self.group_2)
        self.rb_first.setGeometry(QtCore.QRect(10, 20, 83, 16))
        self.rb_first.setCheckable(True)
        self.rb_first.setChecked(False)
        self.rb_first.setObjectName("rb_first")
        self.rb_second = QtWidgets.QRadioButton(self.group_2)
        self.rb_second.setGeometry(QtCore.QRect(10, 50, 83, 16))
        self.rb_second.setObjectName("rb_second")
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

    def InitGUI(self):
        self.btn_confirm.clicked.connect(self.Confirm)

    def Confirm(self):
        path = []
        # 選科目
        if self.rb_basic.isChecked():
            path.append("基礎化學")
        elif self.rb_select.isChecked():
            path.append("選修化學")
        else:
            self.label.setText("請選擇科目!")
            return
        # 選學年
        if self.rb_first.isChecked():
            path.append("上")
        elif self.rb_second.isChecked():
            path.append("下")
        else:
            self.label.setText("請選擇學年!")
            return

        parser = GET_PATH.PathPaser(path)
        aim_path = parser.GetPath()

        print("path = "  + aim_path)
        # testPath = "../database/選修化學/上/"
        try:
            print(os.listdir(aim_path))
        except:
            print("listdir 爆炸了")

        # 透過 Model拿
        # wManager = FetchData.WordManager(aim_path)
        # aim_datas = wManager.ReadWord()





