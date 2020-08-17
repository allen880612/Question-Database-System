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
        for path in path_id:
            qList += SQLExtend.SearchQuestionByPath(self.db, path)
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

    def GetQDSLevelValue(self, findkey):
        return self.QDSLevel.get(findkey, False)

    # 開啟Proxy
    def StartProxy(self):
        exe_name = "cloud_sql_proxy.exe"
        sql_id = "psyched-circuit-286314:asia-east1:xtest00=tcp:3306"
        key_name = "qds_key.json"
        cmd1 = "-instances=" + sql_id
        cmd2 = "-credential_file=" + key_name
        full_cmd = exe_name + " " + cmd1 + " " + cmd2 + " "
        os.popen("cd proxy" + " && " + full_cmd)

    # 連結 SQL資料庫
    def ConnectDatabase(self):
        proxy = threading.Thread(target = self.StartProxy)
        proxy.start()
        proxy.join()

        self.db = mysql.connect(host="35.194.198.56",port=3306,user="user01",passwd="user01",db="QuestionDatabase")