from functools import partial
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from model import MyLibrary
from view.UI import Add_Unit_UI
from view import ComboboxView as cbView
import pathlib
import os

class AddUnitPage(QMainWindow):
    def __init__(self):
        super(AddUnitPage, self).__init__()

        self.ui = Add_Unit_UI.AddUnitPage_UI()
        self.ui.setupUi(self)
        # self.model = _model
        self.Initialize()

    # ��l��
    def Initialize(self):
        pass

    # ���U�ƥ�
    def ConnectEvent(self):
        pass

    # ��l��UI
    def InitUI(self):
        pass