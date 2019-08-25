import pandas as pd
from model import MyLibrary
import os

class ExcelManager():
    def __init__(self, _path):
        self.path = _path #excel的路徑
        self.dataframe = [] #excel的資料表格
        self.isLoad = False

        # 使用者選單用
        self.DefaultString_NoSelect = "NOSELECT"  # 預設未選擇字串
        self.QDSLevel = {}  # QDS的資料層級選單 (下拉式選單用)
        self.QDSLevel[self.DefaultString_NoSelect] = []  # 預設字串先給空
        #

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

    # 創建 下拉選單用的字典
    def CreateDictForLevel(self):
        #region step1: 取得不重複的前五項
        testlist = [] #資料表的前五項 (數學, 應用題, 典型應用題, 配合題, 基本型) etc...
        levelList = ["第一層", "第二層", "第三層", "第四層", "第五層"]
        # self.dataframe.shape[0] 取得列數, shape[1] 取得行數
        for nowrow in range(0, self.dataframe.shape[0]):
            rowLevelName = []
            for level in levelList:
                rowLevelName.append(self.dataframe.loc[nowrow][level]) #第 k 列 的前五項 加入list
            testlist.append(tuple(rowLevelName)) #將前五項做成tuple

        setList = MyLibrary.DeleteRepeatElement(testlist) #利用集合 刪除testList的重複元素

        #endregion
        '''' #test
        for i in range(0, len(setList)):
            if "數學" in setList[i] and "應用題" in setList[i]:
                print(setList[i])'''

        #region step2 將前五項做成字典dict
        #目標效果ex: dict["數學"] = ['應用題', '計算題'], dict[("數學", "應用題")] = ["典型應用題", "非典型應用題"] etc
        #將前項做成key，內容物是後項
        # nowSetList is a tuple
        for nowSetList in setList: #遍歷setList每個元素 (list 裡面各種tuple)
            tempKeyList = [] #做key的過渡List
            self.QDSLevel[self.DefaultString_NoSelect].append(nowSetList[0])
            for nowIndex in range(len(nowSetList) - 1):
                tempKeyList.append(nowSetList[nowIndex]) #將setList的元素逐一加入tempList
                dictkey = MyLibrary.CreateDictKey(tempKeyList) #tempList做成字典用的key (單一元素 or tuple)

                if dictkey not in self.QDSLevel.keys():  # 字典為空
                    self.QDSLevel[MyLibrary.CreateDictKey(tempKeyList)] = [] #字典為空時先給一個空串列

                self.QDSLevel[MyLibrary.CreateDictKey(tempKeyList)].append(nowSetList[nowIndex + 1]) #添加後項

        print("\n-----------")
        print("Get Dict Level")
        print(self.QDSLevel)

        # 刪除重複元素
        for nowDictKey in self.QDSLevel.keys():
            self.QDSLevel[nowDictKey] = MyLibrary.DeleteRepeatElement(self.QDSLevel[nowDictKey])

        print("\n-----------")
        print("Delete repeat")
        print(self.QDSLevel)
        #endregion

    #是否成功讀取excel
    def IsLoad(self):
        return self.isLoad