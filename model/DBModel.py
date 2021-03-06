from model import MyLibrary
from model import SQLExtend
import os
import pymysql as mysql
import threading

class DBModel():
    def __init__(self):
        self.db = None
        self.ConnectDatabase()

        # 仿造 下拉式選單
        self.DefaultString_NoSelect = "NOSELECT"
        self.QDSLevel = {}
        self.CreateQDSLevel()

    # 得到題目List
    # qList = modelv2.GetQuestionList([["數學", "盈虧問題", "基本型"], ["數學", "盈虧問題", "份數轉化"]])
    def GetQuestionList(self, question_level):
        path_id = SQLExtend.SearchPathId(self.db, question_level)
        qList = []
        # 添加填充題
        for path in path_id:
            qList += SQLExtend.SearchQuestionByPath(self.db, path)
        # 添加選擇題
        for path in path_id:
            qList += SQLExtend.SearchSelectQuestionByPath(self.db, path)

        count = 0
        for question in qList:
            question.question_number = int(count + 1)
            count += 1
        return qList

    # 創建 QDSLevel
    def CreateQDSLevel(self):
        path_list = SQLExtend.GetTotalPath(self.db)
        self.QDSLevel[self.DefaultString_NoSelect] = []
        for path in path_list:
            tmp_level = [] # [數學] -> [數學 盈虧問題] -> [數學 盈虧問題 基本型]
            for level in path:
                # 第一層 且 level不再字典中
                if len(tmp_level) == 0:
                    if level not in self.QDSLevel[self.DefaultString_NoSelect]:
                        self.QDSLevel[self.DefaultString_NoSelect].append(level)
                # 其他層
                else:
                    dict_key = MyLibrary.CreateDictKey(tmp_level)
                    if not self.QDSLevel.get(dict_key):
                        self.QDSLevel[dict_key] = []
                    if level not in self.QDSLevel[dict_key]:
                        self.QDSLevel[dict_key].append(level)

                tmp_level.append(level)

    # 檢查路徑是否存在
    def IsPathExist(self, path):
        path_list = SQLExtend.GetTotalPath(self.db)
        return path in path_list

    # 新增一條 新的path (path = [str, str, str..])
    def AddPath(self, path):
        subject_id = SQLExtend.GetSubjectId(self.db, path[0])
        level1_id = SQLExtend.GetLevel1Id(self.db, path[1])
        level2_id = SQLExtend.GetLevel2Id(self.db, path[2])

        # 三個Table 建立資料
        if subject_id is None:
            SQLExtend.InsertSubject(self.db, path[0])
            subject_id = SQLExtend.GetSubjectId(self.db, path[0])

        if level1_id is None:
            SQLExtend.InsertLevel1(self.db, path[1])
            level1_id = SQLExtend.GetLevel1Id(self.db, path[1])

        if level2_id is None:
            SQLExtend.InsertLevel2(self.db, path[2])
            level2_id = SQLExtend.GetLevel2Id(self.db, path[2])

        
        SQLExtend.InsertPath(self.db, [subject_id, level1_id, level2_id])
        print("insert path")

    # 新增填充問題 (type(newQuestion) = class.Question, question_level = [str, str, str], type(imageList) = list[class.QDSTempImage])
    def AddFillingQuestion(self, newQuestion, question_level, imageList):
        path_id = SQLExtend.SearchPathId(self.db, question_level)
        q_id = SQLExtend.InsertFillingQuestion(self.db, newQuestion, path_id[0])
        newQuestion.id = q_id

        for qds_temp_image in imageList:
            self.AddImage(q_id, newQuestion.GetType(), qds_temp_image.GetBytes())

        # 新增詳解
        self.AddSolution(newQuestion)

    # 編輯填充問題
    def EditFillingQuestion(self, editQuestion):
        SQLExtend.UpdateFillingQuestion(self.db, editQuestion)
        # 填充題的image list 更新在別的地方

    # 新增選擇題
    def AddSelectQuestion(self, newQuestion, question_level):
        path_id = SQLExtend.SearchPathId(self.db, question_level)
        q_id = SQLExtend.InsertSelectQuestion(self.db, newQuestion, path_id[0])
        newQuestion.id = q_id
        print(newQuestion.GetType())

        # 新增題目圖片
        for qds_temp_image in newQuestion.GetImages():
            self.AddImage(q_id, newQuestion.GetType(), qds_temp_image.GetBytes())
        # 新增選項圖片
        for v in newQuestion.option:
            option_type = v.GetType()
            option_imageList = v.GetImages()
            for qds_temp_image in option_imageList:
                self.AddImage(q_id, option_type, qds_temp_image.GetBytes())

    # 編輯選擇題
    def EditSelectQuestion(self, question):
        SQLExtend.UpdateSelectQuestion(self.db, question)

        # todo -> add image to database
        # 處理圖片
        self.UpdateDBImageList(question.GetImages(), question.id, question.GetType())
        for v in question.option:
            self.UpdateDBImageList(v.GetImages(), question.id, v.GetType())

    # 刪除題目
    def DeleteQuestion(self, question):
        if question.GetType() == "FillingQuestion":
            # 刪除圖片
            for image in question.GetImages():
                self.DeleteImage(image)
            # 刪除詳解
            self.DeleteSolution(question)
            # 刪除題目
            SQLExtend.DeleteFillingQuestion(self.db, question)

        elif question.GetType() == "SelectQuestion":
            # 刪除圖片
            for image in question.GetImages():
                self.DeleteImage(image)
            # 刪除選項的圖片
            for option in question.option:
                for image in option.GetImages():
                    self.DeleteImage(image)
            # 刪除詳解
            self.DeleteSolution(question)
            # 刪除題目
            SQLExtend.DeleteSelectQuestion(self.db, question)
            
    # 新增圖片
    def AddImage(self, question_id, source, image_blob):
        SQLExtend.InsertImage(self.db, question_id, source, image_blob)

    # 刪除圖片
    def DeleteImage(self, image):
        SQLExtend.DeleteImageById(self.db, image.Id)

    # 更新資料庫裡的圖片
    def UpdateDBImageList(self, imageList, q_id, q_type):
        for image in imageList:
            if image.IsUpdated:
                if image.IsOnServer == True and image.IsShowOnListWidget == False:
                    self.DeleteImage(image) # 刪除圖片
                elif image.IsOnServer == False and image.IsShowOnListWidget == True:
                    self.AddImage(q_id, q_type, image.GetBytes()) # 新增圖片
                    image.IsOnServer = True
    
    # 新增詳解
    def AddSolution(self, question):
        solution = question.GetSolution()
        if solution is None:
            return

        SQLExtend.InsertSolution(self.db, question.id, question.GetType(), solution)
        self.UpdateDBImageList(solution.GetImages(), question.id, solution.GetType())

    # 更新詳解
    def UpdateSolution(self, question):
        solution = question.GetSolution()
        if solution is None:
            return

        SQLExtend.UpdateSolution(self.db, question.id, question.GetType(), solution)
        self.UpdateDBImageList(solution.GetImages(), question.id, solution.GetType())

    # 刪除詳解
    def DeleteSolution(self, question):
        solution = question.GetSolution()
        if solution is None:
            return

        for image in solution.GetImages():
            self.DeleteImage(image)

        SQLExtend.DeleteSolution(self.db, solution)
        question.SetSolution(None)

    # 用question 得到圖片群
    def GetImagesByQuestion(self, question):
        images = SQLExtend.SearchImageByQuestion(self.db, question.id, question.GetType())
        imageList = []
        for image in images:
            image_id = image[0]
            image_content = image[1]
            qds_temp_image = MyLibrary.QDSTempImage(image_content, image_id, isOnServer=True, isUpdated=False)
            imageList.append(qds_temp_image)

        return imageList


    # 得到所有的科目 (return list)
    def GetSubjectNameList(self):
        subject_list = SQLExtend.GetTotalSubjectName(self.db)
        return subject_list

    # 開啟 SQL區

    # 開啟Proxy
    def StartProxy(self):
        exe_name = "cloud_sql_proxy.exe"
        sql_id = "psyched-circuit-286314:asia-east1:xtest00=tcp:3306"
        key_name = "qds_key.json"
        cmd1 = "-instances=" + sql_id
        cmd2 = "-credential_file=" + key_name
        full_cmd = exe_name + " " + cmd1 + " " + cmd2 + " "
        os.popen("cd proxy" + " && " + full_cmd)

    # 使用proxy 連線
    def UseProxy(self):
        proxy = threading.Thread(target = self.StartProxy)
        proxy.start()
        proxy.join()
        self.db = mysql.connect(host="127.0.0.1",port=3306,user="user01",passwd="user01",db="QuestionDatabase")

    # 使用SQL 連線
    def UseSQLIP(self):
        self.db = mysql.connect(host="35.239.126.119",port=3306,user="user01",passwd="user01",db="QDS")

    # 連結 SQL資料庫
    def ConnectDatabase(self):
        #self.UseProxy()
        self.UseSQLIP()