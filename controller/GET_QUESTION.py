import pandas as pd
from model import MyLibrary
import os

class ExcelManager():
    def __init__(self, _path):
        self.path = _path #excel的路徑
        self.dataframe = [] #excel的資料表格
        self.isLoad = False

        print("\n-----------------------------")
        self.ReadExcel()

    #讀取excel
    def ReadExcel(self):
        #need to pip xlrd
        print("read path: " + self.path)
        try:
            self.dataframe = pd.read_excel(self.path)
            print(self.dataframe)
            self.isLoad = True
        except:
            print("load fail")

        print("\n-----------------")

    #取得excel中指定的題目
    def GetFilteredQuestion(self, questionType):
        # df.loc[('bar', 'two'), 'A'] tuple法不能用，因為數學、應用題那些不屬於index
        flagList1 = ["第一層", "第二層", "第三層", "第四層", "第五層"]
        #flagType = ["數學", "應用題", "典型應用題", "盈虧問題", "基本型"]
        # flag = self.dataframe[flagList1] == flagType
        flag = True
        for i in range(0, len(questionType)):
            tempFlag = (self.dataframe[flagList1[i]] == questionType[i])
            flag = flag & tempFlag
        # & & &&& 過濾器法
        question = self.dataframe[flag]["題目"] #question = 過濾後的題目 (type(question) = Series)
        return list(question) #Convert to list

        '''flag = self.dataframe[level] == questionType #過濾器條件
        filter_dataframe = self.dataframe[flag] #過濾後的資料表格
        questionList = filter_dataframe["題目"]
        questionList = list(questionList) #串列化過濾後的表格
        #print(len(questionList))
        return questionList'''


    def GetFilteredImage(self, questionType):
        # df.loc[('bar', 'two'), 'A'] tuple法不能用，因為數學、應用題那些不屬於index
        flagList1 = ["第一層", "第二層", "第三層", "第四層", "第五層"]
        #flagType = ["數學", "應用題", "典型應用題", "盈虧問題", "基本型"]
        # flag = self.dataframe[flagList1] == flagType
        flag = True
        for i in range(0, len(questionType)):
            tempFlag = (self.dataframe[flagList1[i]] == questionType[i])
            flag = flag & tempFlag
        # & & &&& 過濾器法
        image = self.dataframe[flag]["圖"] #question = 過濾後的題目 (type(question) = Series)
        print(image)
        imageList = []
        for i in image:
            imageList.append(i.split(' '))
        print(imageList)
        return imageList

    #是否成功讀取excel
    def IsLoad(self):
        return self.isLoad

    def GetOriginalDataFrame(self):
        return self.dataframe