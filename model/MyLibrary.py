import os
import docx
import copy
import numpy as np

# 刪除串列中重複的元素 (然後照加入順序排)
def DeleteRepeatElement(oldList):
    newList = list(set(oldList))  # 以集合刪除重複tuple
    newList.sort(key=oldList.index)  # 照原本順序排好
    return newList

# 建構字典的key
def CreateDictKey(keyList):
    if len(keyList) == 1:  # key only have 1 element
        return keyList[0]
    else:
        return tuple(keyList)

# Question Class
class Question(object):
    def __init__(self, question, images, imgPath, indexOnExcel, qnumber=0):
        self.__questionAnswer = question
        self.__haveImage = True
        self.__question = self.DeleteAnswer(question)
        self.__image = self.PaserImage(images, imgPath)
        self.__images = images
        self.__imagePath = imgPath
        self.__question_number = qnumber
        self.dataframe_index = indexOnExcel

    def PaserImage(self, images, imgPath):
        # 篩掉無圖片的
        # if not images:
        if images == "NOIMAGE":
            self.__haveImage = False
            # print("parser direct", self.__haveImage) # wtf
            # self.SetHaveImage(False)
            # print("parser set", self.__haveImage)  # wtf
            return False
        # 用空格分多圖片路徑，存至list
        imageList = []
        tmpPaths = images.split(' ')
        for img in tmpPaths:
            imageList.append(imgPath + "\\" + img)  # 遍歷補路徑
        self.__haveImage = True
        return imageList

    def GetImage(self):
        return self.__image

    def HaveImage(self):
        return self.__haveImage

    # 返回 不帶路徑的圖片名
    def GetImages(self):
        return self.__images

    def SetHaveImage(self, flag):
        self.__haveImage = flag

    def GetQuestionAnswer(self):
        return self.__questionAnswer

    def GetQuestion(self):
        return self.__question

    def GetQuestionNumber(self):
        return self.__question_number

    def DeleteAnswer(self, str):
        newQuestion = ""
        addMode = True  # Mode = True > add a char, False > add a space

        for ch in str:
            if addMode == True or ch == '】':
                newQuestion += ch
            elif addMode == False:
                newQuestion += ' '

            if ch == '【':
                addMode = False
            elif ch == '】':
                addMode = True
        return newQuestion
    
    # 編輯問題
    def EditQuestion(self, new_question, images=""):
        self.__questionAnswer = new_question
        self.__question = self.DeleteAnswer(new_question)
        if images != "" and self.__images != images:
            print("TrueTrueTrue")
            self.__images = images
            self.__image = self.PaserImage(images, self.__imagePath)

    # 轉換成data frame 使用的list
    def ConvertToList(self, question_level):
        q_info = copy.deepcopy(question_level)
        q_info.append("") # Level 3
        q_info.append("") # Level 4
        q_info.append("") # Level 5
        q_info.append(self.GetQuestionNumber()) # 題號
        q_info.append(self.GetQuestionAnswer()) # 題目含答案
        q_info.append("NOIMAGE" if not self.HaveImage() else self.GetImages()) # 圖片
        q_info.append(self.dataframe_index) # 編號 on Dataframe
        return q_info

#建構篩選好的問題List
def CreatQuestionList(df, questionType):
    questionList = []
    imagePath = "database\\" + "\\".join(questionType)  # base path
    for index, row in df.iterrows():
        questionList.append(Question(row["題目"], row["圖"], imagePath, row["編號"], row["題號"]))
        #print(row)
        #print(row["題目"], row["圖"])
    # for q in questionList:
    #     print(q.GetQuestion(), q.GetImage())
    return questionList

# 依照list 取得資料夾路徑
def GetFolderPathByList(dir_list):
    dir_path = "database"
    for dir in dir_list:
        dir_path = os.path.join(dir_path, dir)
    return dir_path

# 檔案是否存在
def IsFileExist(file_path):
    return os.path.isfile(file_path)

# Word 是否被打開 (不檢查是否有檔案)
def IskWordOpen(file_path):
    if not IsFileExist(file_path):
        return True
    flag = True
    try:
        word = docx.Document(file_path)
        word.save(file_path)
    except:
        flag = False
    print(flag)
    return flag

# 得到顯示用的題目文字 (Ex: 盈虧問題 - 基本題) (add_question_strlist = ["盈虧問題 - 基本題"])
def GetQuestionShowText(add_question_strlist):
    return " - ".join(add_question_strlist)

# 檢查list 維度
def CheckListDimension(check_list):
    dimesion = 0
    while type(check_list) == list:
        dimesion += 1
        check_list = check_list[0]
    return dimesion

#######################
#temp
def DeleteAnswer(str):
    newQuestion = ""
    addMode = True  # Mode = True > add a char, False > add a space

    for ch in str:
        if addMode == True or ch == '】':
            newQuestion += ch
        elif addMode == False:
            newQuestion += ' '

        if ch == '【':
            addMode = False
        elif ch == '】':
            addMode = True
    return newQuestion