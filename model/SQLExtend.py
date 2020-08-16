import pymysql as mysql
from model import MyLibrary
# 科目 類型 題型 兩個問題 圖片 大概6個Table

# 執行 插入 / 更新 / 刪除等 修改資料庫的指令
def ExecuteAlterCommand(database, query):
	handler = database.cursor()
	try:
		handler.execute(query)
		database.commit()
	except:
		database.rollback()

# 插入一個科目
def InsertSubject(database, subject_name):
	query = "INSERT INTO Subject VALUES ('{0}');".format(subject_name)
	ExecuteAlterCommand(database, query)

# 插入一個Level1 (etc 盈虧問題 燕尾定理)
def InsertLevel1(database, level1_name):
	query = "INSERT INTO Level1 VALUES ('{0}');".format(level1_name)
	ExecuteAlterCommand(database, query)

# 插入一個Level2 (etc 基本型 倍數轉化)
def InsertLevel2(database, level2_name):
	handler = database.cursor()
	handler.execute("SELECT COUNT(`Id`) FROM Level2;")
	id = int(handler.fetchone()[0])
	query = "INSERT INTO Level2 VALUES ({0}, '{1}');".format(id, level2_name)
	ExecuteAlterCommand(database, query)

# 插入填充題
def InsertFillingQuestion(database, answer, solution=None, image=None):
	handler = database.cursor()
	handler.execute("SELECT COUNT(`Id`) FROM FillingQuestion;")
	id = int(handler.fetchone()[0])
	content = MyLibrary.DeleteAnswer(answer)
	query = "INSERT INTO FillingQuestion (`Id`, `Content`, `Answer`, `Solution_Id`) VALUES ({0}, '{1}', '{2}', {3});".format(id, content, answer, "NULL")
	ExecuteAlterCommand(database, query)

# 更新 Subject 的名字
def UpdateLevel1Name(database, id, subject):
	query = "UPDATE Subject SET `Name`='{0}' WHERE Id={1};".format(subject, id)
	ExecuteAlterCommand(database, query)

# 更新 Level1 的名字
def UpdateLevel1Name(database, id, level1_name):
	query = "UPDATE Level1 SET `Name`='{0}' WHERE Id={1};".format(level1_name, id)
	ExecuteAlterCommand(database, query)

# 更新 Level2 的名字
def UpdateLevel2Name(database, id, level2_name):
	query = "UPDATE Level2 SET `Name`='{0}' WHERE Id={1};".format(level2_name, id)
	ExecuteAlterCommand(database, query)

# 搜尋路徑的Id (return list)
def SearchPathId(database, question_level=[[]]):
	# SELECT PathTable.Id, Subject.Name, Level1.Name, Level2.Name
	# FROM Subject, Level1, Level2
	# NATURAL JOIN PathTable
	# WHERE (Subject.Id=PathTable.Subject_Id and Level1.Id=PathTable.Level1_Id and Level2.Id=PathTable.Level2_Id) and ((Subject.Name="數學" and Level1.Name="盈虧問題" and Level2.Name="基本型") or (Subject.Name="數學" and Level1.Name="盈虧問題" and Level2.Name="份數轉化"))
	
	handler = database.cursor()
	pre_query = "SELECT PathTable.Id, Subject.Name, Level1.Name, Level2.Name FROM Subject, Level1, Level2 NATURAL JOIN PathTable "
	condition1 = "WHERE (Subject.Id=PathTable.Subject_Id and Level1.Id=PathTable.Level1_Id and Level2.Id=PathTable.Level2_Id)"
	
	condition_list = []
	for level in question_level:
		condition = "(Subject.Name='{0}' and Level1.Name='{1}' and Level2.Name='{2}')".format(level[0], level[1], level[2])
		condition_list.append(condition)
	condition = " or ".join(condition_list)
	condition = "({0})".format(condition)

	query = ""
	if condition_list == []:
		query = pre_query + condition1
	else:
		query = pre_query + condition1 + " and " + condition

	handler.execute(query)
	path_id = [int(tup[0]) for tup in handler.fetchall()]
	return path_id

# 以路徑搜尋Question (return Question List)
def SearchQuestionByPath(database, path_id):
	handler = database.cursor()
	query = "SELECT * FROM FillingQuestion WHERE FillingQuestion.Path_Id={0};".format(str(path_id))
	handler.execute(query)
	result = handler.fetchall()
	qList = []
	count = 0
	for data in result:
		qList.append(MyLibrary.Question(data[2], "NOIMAGE", "0", 0, qnumber=count))
		count+=1
	return qList

# 得到所有科目的名稱 (return list:[str])
def GetTotalSubjectName(database):
	handler = database.cursor()
	query = "SELECT Subject.Name FROM Subject;"
	handler.execute(query)
	subject_name_list = [name[0] for name in handler.fetchall()]
	return subject_name_list

# 得到所有Level1的名稱 (return list:[str])
def GetTotalLevel1Name(database):
	handler = database.cursor()
	query = "SELECT Level1.Name FROM Level1;"
	handler.execute(query)
	level1_name_list = [name[0] for name in handler.fetchall()]
	return level1_name_list

# 藉由subject 得到 level1
def GetLevel1NameBySubject(database, subject):
	handler = database.cursor()
	pre_query = "SELECT Level1.Name FROM Subject, Level1, Level2 NATURAL JOIN PathTable WHERE (Subject.Id=PathTable.Subject_Id and Level1.Id=PathTable.Level1_Id and Level2.Id=PathTable.Level2_Id)"
	condition = "(Subject.Name='{0}')".format(subject)
	query = pre_query + " and " + condition
	handler.execute(query)
	level1_name_list = [name[0] for name in handler.fetchall()]
	return level1_name_list

# 得到所有Level2的名稱 (return list:[str])
def GetTotalLevel2Name(database):
	handler = database.cursor()
	query = "SELECT Level1.Name FROM Level1;"
	handler.execute(query)
	level2_name_list = [name[0] for name in handler.fetchall()]
	return level2_name_list

# 藉由subject, level1 得到 level2
def GetLevel2NameByLevel1(database, subject, level1):
	handler = database.cursor()
	pre_query = "SELECT Level1.Name FROM Subject, Level1, Level2 NATURAL JOIN PathTable WHERE (Subject.Id=PathTable.Subject_Id and Level1.Id=PathTable.Level1_Id and Level2.Id=PathTable.Level2_Id)"
	condition = "(Subject.Name='{0} and Level1.Name={1}')".format(subject, level1)
	query = pre_query + " and " + condition
	handler.execute(query)
	level2_name_list = [name[0] for name in handler.fetchall()]
	return level2_name_list