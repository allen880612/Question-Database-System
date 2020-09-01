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
    
    solution_signal = QtCore.pyqtSignal(bool, list) # set 信號

    def __init__(self, _model):
        super(AddSolutionPage, self).__init__()

        self.ui = Add_Solution_UI.AddSolutionPage_UI()
        self.ui.setupUi(self)
        self.model = _model

        self.Solution = None
        self.temp_importImage = None
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
            self.temp_importImage = None
            self.imageList = []
            self.UpdateImageListWidget()
            self.ui.textEdit_solution.setPlainText("")
        # 有詳解的情況
        else:
            self.temp_importImage = None
            self.imageList = copy.deepcopy(self.Solution.GetImages())
            self.UpdateImageListWidget()
            self.ui.textEdit_solution.setPlainText(self.Solution.GetContent())

        self.UpdateUI()

    # 註冊事件
    def ConnectEvent(self):
        self.ui.button_back_page.clicked.connect(self.ClosePage)
        self.ui.button_store.clicked.connect(self.StoreSolution)
        self.ui.button_add_image.clicked.connect(self.ImportImage)
        self.ui.button_add_list.clicked.connect(self.ImageAddToList)
        self.ui.button_delete_image.clicked.connect(self.DeleteImage)
        self.ui.list_widget_image.currentItemChanged.connect(self.SelectImage)

    # 更新UI
    def UpdateUI(self):
        self.ui.button_add_list.setEnabled(self.temp_importImage is not None)
        self.ui.button_delete_image.setEnabled(self.ui.list_widget_image.currentRow() >= 0)

    # 匯入圖片
    def ImportImage(self):
        img_path = QFileDialog.getOpenFileName(self, '插入圖片', 'c\\', 'Image files (*.jpg *.png)')
        file_name = img_path[0] #img_path[0] = absolate path of image
        if file_name == "":
            return

        byte_content = MyLibrary.ConvertToBinaryData(file_name) # binary data
        newTempImage = MyLibrary.QDSTempImage(byte_content)
        self.temp_importImage = newTempImage

        self.ui.label_preview_image.setPixmap(newTempImage.GetFormatPixmap())
        self.UpdateUI() # 更新UI

    # 圖片++list
    def ImageAddToList(self):
        image_text = self.ui.list_widget_image.count() + 1
        self.imageList.append(self.temp_importImage)
        self.ui.list_widget_image.addItem(str(image_text))
        self.temp_importImage = None

        self.ui.label_preview_image.clear() # 清空預覽圖片
        self.UpdateUI()

    # 刪除圖片
    def DeleteImage(self):
        nowSelectImageIndex = self.ui.list_widget_image.currentRow() # Get Current Row Index

        if nowSelectImageIndex == -1:
            return

        image_index = self.GetImageIndex(nowSelectImageIndex)
        select_image = self.imageList[image_index]
        # 圖片存在Server上
        if select_image.IsOnServer:
            select_image.IsUpdated = True
            select_image.IsShowOnListWidget = False
            print("image - onserver delete")
        # 圖片不存在於Server上
        else:
            self.imageList.pop(image_index)
            print("image - not onserver delete")

        self.UpdateImageListWidget()

    # 選擇圖片
    def SelectImage(self):
        nowSelectImageIndex = self.ui.list_widget_image.currentRow() # Get Current Row Index

        if nowSelectImageIndex == -1:
            self.ui.label_preview_image.clear()
            return

        image_index = self.GetImageIndex(nowSelectImageIndex)
        select_image = self.imageList[image_index]
        self.ui.label_preview_image.setPixmap(select_image.GetFormatPixmap()) # 設置圖片

        self.UpdateUI()

    def GetImageIndex(self, nowSelectImageIndex):
        image_index = 0
        temp_index = 0
        for image in self.imageList:
            if image.IsShowOnListWidget: # 如果他在list widget中
                if temp_index == nowSelectImageIndex: # 而且index = 所選的列
                    break
                else:
                    temp_index += 1
            image_index += 1
        return image_index

    def UpdateImageListWidget(self):
        k = 1
        self.ui.list_widget_image.clear()
        for image in self.imageList:
            if image.IsShowOnListWidget:
                self.ui.list_widget_image.addItem(str(k))
                k += 1

    # 設置詳解
    def SetSolution(self, solution):
        #print(str(id(self.Solution)) + " " + str(id(solution)))
        self.Solution = MyLibrary.QDSSolution(-1, "")

        if solution is not None:
            self.DeepCopySolution(self.Solution, solution)

    # 儲存詳解
    def StoreSolution(self):
        self.Is_store = True
        self.Solution.SetContent(self.ui.textEdit_solution.toPlainText())
        self.Solution.Images = copy.deepcopy(self.imageList)

    # 深層複製 b -> a
    def DeepCopySolution(self, a, b):
        a.Id = b.Id
        a.SetContent(b.GetContent())
        a.Images = copy.deepcopy(b.GetImages())

    # 關閉視窗
    def ClosePage(self):
        self.is_click_button = True
        is_close = self.close()
        self.ReturnSolution(is_close)

    # 關閉視窗事件
    def closeEvent(self, event):
        # 不是透過按鈕來關閉視窗 > 同關閉
        if self.is_click_button == False:
            is_close = True
            self.ReturnSolution(is_close)

    # 回傳Solution
    def ReturnSolution(self, is_close):
        if self.Is_store == True:
            self.solution_signal.emit(is_close, [self.Solution])
        else:
            self.solution_signal.emit(is_close, [None])