import pandas as pd
import os

class ExcelManager():
    def __init__(self, _path):
        self.path = _path #excel的路徑
        self.dataframe = []
        self.isLoad = False
        print("\n-----------------------------")
        self.ReadExcel()

    #讀取excel
    def ReadExcel(self):
        print("read path: " + self.path)
        try:
            self.dataframe = pd.read_excel(self.path)
            print(self.dataframe)
            self.isLoad = True
        except:
            print("load fail")

        print("\n-----------------")

    #取得excel中的第k層 xx類型
    def GetFilteredQuestion(self, level, questionType):
        flag = self.dataframe[level] == questionType #過濾器條件
        filter_dataframe = self.dataframe[flag] #過濾後的資料表格
        questionList = filter_dataframe["題目"]
        questionList = list(questionList) #串列化過濾後的表格
        #print(len(questionList))
        return questionList

    #是否成功讀取excel
    def IsLoad(self):
        return self.isLoad