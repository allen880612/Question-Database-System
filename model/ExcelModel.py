import pandas as pd
from model import MyLibrary
import os


class ExcelModel():
    def __init__(self, _path):
        self.path = _path #excel的路徑
        self.dataframe = pd.DataFrame() #excel的資料表格
        self.filleredDataframe = []
        self.isLoad = False
        self.qaList = []
        self.qList = []
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

    #過濾表格
    def GetFilteredDataframe(self, questionType):
        # df.loc[('bar', 'two'), 'A'] tuple法不能用，因為數學、應用題那些不屬於index
        flagList1 = ["第一層", "第二層", "第三層", "第四層", "第五層"]
        # flagType = ["數學", "應用題", "典型應用題", "盈虧問題", "基本型"]
        # flag = self.dataframe[flagList1] == flagType
        flag = True
        for i in range(0, len(questionType)):
            tempFlag = (self.dataframe[flagList1[i]] == questionType[i])
            flag = flag & tempFlag
        # & & &&& 過濾器法
        self.filleredDataframe = self.dataframe[flag] #過濾後的題目 (type() = dataframe)
        quesImage_df = self.filleredDataframe.loc[:, ["題目", "圖"]]
        self.qList = MyLibrary.CreatQuestionList(quesImage_df.reset_index(), questionType) #建構question list
        print("GetFilteredDataframe done")

    def GetQuestionList(self):
        return self.qList

    # 直接拿題目列表
    def GetQuestionList(self, questionType):
        self.GetFilteredDataframe(questionType)
        return self.qList

    # 添加問題
    def AddQuestion(self, questionInfo):
        self.dataframe = self.dataframe.append(questionInfo, ignore_index=True)
        print(self.dataframe.tail(1))
        self.WriteToExcel()

    # 寫檔到Excel
    def WriteToExcel(self):
        print(os.getcwd(), self.path)
        self.dataframe.to_excel(self.path, index=False)

    # #取得excel中指定的題目
    # def GetFilteredQuestion(self):
    #   74  return list(self.filleredDataframe["題目"]) #Convert to list
    #
    # #取得圖
    # def GetFilteredImage(self, questionType):
    #     imagePath = "database\\" + "\\".join(questionType)  # base path
    #     image = self.filleredDataframe["圖"]
    #     imageList = []
    #     for im in list(image):
    #         tempImage = im.split(' ')
    #         if im != "NOIMAGE":
    #             for i in range(0, len(tempImage)):
    #                 tempImage[i] = imagePath + "\\" + tempImage[i] # 遍歷補路徑
    #         imageList.append(tempImage)
    #     return imageList

    # 是否成功讀取excel
    def IsLoad(self):
        return self.isLoad

    def GetOriginalDataFrame(self):
        return self.dataframe