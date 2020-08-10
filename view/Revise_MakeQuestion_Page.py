from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtWidgets, QtGui
from view.UI import Revise_MakeQuestion_UI 
from view import ComboboxView as cbview
from model import MyLibrary
import random
import os
import docx

class ReviseMakeQuestionPage(QMainWindow):

    def __init__(self, _model):
        super(ReviseMakeQuestionPage, self).__init__()
        self.ui = Revise_MakeQuestion_UI.ReviseMakeQuestion_UI()
        self.ui.setupUi(self)
        self.model = _model

    # 重設頁面
    def ResetPage():
        pass