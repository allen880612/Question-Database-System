from functools import partial
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets
from model import MyLibrary
from view.UI import Add_Solution_UI
from view import ComboboxView as cbView
import pathlib
import os
import copy

class AddSolutionPage(QMainWindow):
    
    solution_signal = QtCore.pyqtSignal(bool, MyLibrary.QDSSolution) # set 信號

    def __init__(self, _model):
        super(AddSolutionPage, self).__init__()

        self.ui = Add_Solution_UI.AddSolutionPage_UI()
        self.ui.setupUi(self)
        self.model = _model

        self.Solution = None
        self.temp_import_image = None
        self.Is_store = False
        self.imageList = []

        self.is_click_button = False
        self.Initialize()

    # 初始化
    def Initialize(self):
        self.ConnectEvent()
        self.UpdateUI()

    # 重設頁面
    def ResetPage(self):
        self.is_click_button = False
        self.Is_store = False

        # 沒有詳解的情況
        if self.Solution is None:
            self.temp_import_image = None
            self.imageList = []
            # todo: Reset Image ListWidget
            self.ui.textEdit_solution.setPlainText("")
        # 有詳解的情況
        else:
            self.temp_import_image = None
            self.imageList = self.Solution.GetImages()
            self.ui.textEdit_solution.setPlainText(self.Solution.GetContent())

        self.UpdateUI()

    # 註冊事件
    def ConnectEvent(self):
        self.ui.button_back_page.clicked.connect(self.ClosePage)
        self.ui.button_store.clicked.connect(self.StoreSolution)

    # 更新UI
    def UpdateUI(self):
        pass

    # 設置詳解
    def SetSolution(self, solution):
        #print(str(id(self.Solution)) + " " + str(id(solution)))
        if solution is None:
            self.Solution = MyLibrary.QDSSolution(-1, "")
        else:
            self.DeepCopySolution(self.Solution, solution)

    # 儲存詳解
    def StoreSolution(self):
        self.Is_store = True

    # 深層複製 b -> a
    def DeepCopySolution(self, a, b):
        a.Id = b.Id
        a.SetContent(b.GetContent())
        a.Images = copy.deepcopy(b.GetImages())

    # 關閉視窗
    def ClosePage(self):
        self.is_click_button = True
        is_close = self.close()
        if self.Is_store == True:
            self.solution_signal.emit(is_close, self.Solution)
        else:
            self.solution_signal.emit(is_close, None)

    # 關閉視窗事件
    def closeEvent(self, event):
        # 不是透過按鈕來關閉視窗 > 同關閉
        if self.is_click_button == False:
            is_close = True
            self.solution_signal.emit(is_close, None)