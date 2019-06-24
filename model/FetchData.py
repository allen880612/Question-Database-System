import json
import sys 
sys.path.append('../controller')
sys.path.append('../model')
import pandas as pd
import os

class WordManager():
    def __init__(self, _path):
        self.path = _path

    def ReadWord(self):
        # auaupath = "../database/選修化學/上"
        print("reader path : " + self.path)
        # aim_datas = os.listdir(self.path)
        try:
            print(os.listdir(self.path))
        except:
            print("explosion")
        finally:
            print("fuck your module")
        # file = docx.Document("")








