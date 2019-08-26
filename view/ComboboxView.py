from PyQt5 import QtCore, QtGui, QtWidgets
from model import MyLibrary
class ComboboxManager():
    def __init__(self, _dataframe):
        self.dataframe = _dataframe
        # 使用者選單用
        self.DefaultString_NoSelect = "NOSELECT"  # 預設未選擇字串
        self.QDSLevel = {}  # QDS的資料層級選單 (下拉式選單用)
        self.QDSLevel[self.DefaultString_NoSelect] = []  # 預設字串先給空
        #

        self.CreateDictForLevel()

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

    def GetQDSLevel(self):
        return self.QDSLevel

    def GetDictValue(self, findkey):
        return self.QDSLevel[findkey]

    def GetNoSelectString(self):
        return self.DefaultString_NoSelect
