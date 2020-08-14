import pymysql as mysql
import threading
import os
from model import SQLExtend

# 測試資料庫
def TestDB(myDB):
    cHandler = myDB.cursor()
    query = "SHOW DATABASES;"
    cHandler.execute(query)
    result = cHandler.fetchall()

    for row in result:
        print (row)

def CreateTabel_Subject(database):
    handler = database.cursor()
    query = "CREATE TABLE Subject (Name varchar(50));"
    handler.execute(query)

def CreateTabel_Level(database, num):
    handler = database.cursor()
    query = "CREATE TABLE Level" + str(num) +  " (Name varchar(50));"
    handler.execute(query)

def CreateTabel_FillingQuestion(database):
    handler = database.cursor()
    query = "CREATE TABLE FillingQuestion (Id INT, Number INT, Content varchar(1024), Answer varchar(1024), Solution_Id INT);"
    handler.execute(query)

def CreateTabel_QuestionSolution(database):
    handler = database.cursor()
    query = "CREATE TABLE Solution (Id INT, Content varchar(1024));"
    handler.execute(query)

def ShowTable(database):
    handler = database.cursor()
    query = "SHOW TABLE;"
    handler.execute(query)

    result = handler.fetchall()

    for row in result:
        print (row)

def ShowSubject(database):
    handler = database.cursor()
    handler.execute("USE QuestionDatabase;")
    query = "SELECT * FROM Subject;"
    handler.execute(query)

    result = handler.fetchall()

    for row in result:
        print (row)

def ShowLevel1(database):
    handler = database.cursor()
    handler.execute("USE QuestionDatabase;")
    query = "SELECT * FROM Level1;"
    handler.execute(query)

    result = handler.fetchall()

    for row in result:
        print (row)

def ShowLevel2(database):
    handler = database.cursor()
    handler.execute("USE QuestionDatabase;")
    query = "SELECT * FROM Level2;"
    handler.execute(query)

    result = handler.fetchall()

    for row in result:
        print (row)

# 開啟Proxy
def StartProxy():
    exe_name = "cloud_sql_proxy.exe"
    sql_id = "psyched-circuit-286314:asia-east1:xtest00=tcp:3306"
    key_name = "qds_key.json"
    cmd1 = "-instances=" + sql_id
    cmd2 = "-credential_file=" + key_name
    full_cmd = exe_name + " " + cmd1 + " " + cmd2 + " "
    os.popen("cd proxy" + " && " + full_cmd)

if __name__ == '__main__':
    proxy = threading.Thread(target = StartProxy)
    proxy.start()
    proxy.join()
    myDB = mysql.connect(host="127.0.0.1",port=3306,user="user01",passwd="user01",db="QuestionDatabase")
	#db = mysql.connector.connect(host="192.168.179.148",user="newuser",passwd="12345678")