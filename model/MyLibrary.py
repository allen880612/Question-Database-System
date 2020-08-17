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
    def __init__(self, id, content, qnumber=0):
        self.__questionType = "Filling" # 填充題
        self.__answer = content
        self.__haveImage = False
        self.__question = self.DeleteAnswer(content)
        self.__question_number = qnumber
        self.id = id

    def PaserImage(self, images, imgPath):
        # 篩掉無圖片的
        # if not images:
        if images == "NOIMAGE":
            self.__haveImage = False
            return False
        # 用空格分多圖片路徑，存至list
        imageList = []
        tmpPaths = images.split(' ')
        for img in tmpPaths:
            imageList.append(imgPath + "\\" + img)  # 遍歷補路徑
        self.__haveImage = True
        return imageList

    def GetAnswer(self):
        return self.__answer

    def GetQuestion(self):
        return self.__question

    def GetQuestionNumber(self):
        return self.__question_number

    def EditQuestion(self, answer):
        self.__answer = answer
        self.__question = self.DeleteAnswer(answer)

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