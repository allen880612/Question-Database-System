import pymysql as mysql
from model import MyLibrary
# 科目 類型 題型 兩個問題 圖片 大概6個Table

# 執行 插入 / 更新 / 刪除等 修改資料庫的指令 (return cursor)
def ExecuteAlterCommand(database, cursor, query, format_parement=()):
	try:
		if len(format_parement) == 0:
			cursor.execute(query)
		else:
			cursor.execute(query, format_parement)
		database.commit()
	except Exception as e:
		database.rollback()
		print("execute error!")
		print(e)

def GetTableCount(database, table):
	handler = database.cursor()
	query = "SELECT COUNT(*) FROM {0};".format(table)
	handler.execute(query)
	count = int(handler.fetchone()[0])
	return count

# 向Subject, Level1, Level2 Table中插入一條
def InsertToTable(database, table, name):
	cursor = database.cursor()
	query = "INSERT INTO {0} (`Name`) VALUES ('{1}');".format(table, name)
	ExecuteAlterCommand(database, cursor, query)

# 插入一個科目
def InsertSubject(database, subject_name):
	InsertToTable(database, "Subject", subject_name)

# 插入一個Level1 (etc 盈虧問題 燕尾定理)
def InsertLevel1(database, level1_name):
	InsertToTable(database, "Level1", level1_name)

# 插入一個Level2 (etc 基本型 倍數轉化)
def InsertLevel2(database, level2_name):
	InsertToTable(database, "Level2", level2_name)

# 新增一條path (path = [0, 0, 0, 0...])
def InsertPath(database, path):
	cursor = database.cursor()
	query = "INSERT INTO PathTable (`Subject_Id`, `Level1_Id`, `Level2_Id`) VALUES ({0}, {1}, {2});".format(path[0], path[1], path[2])
	ExecuteAlterCommand(database, cursor, query)

# 插入填充題
def InsertFillingQuestion(database, question, path_id, solution=None, image=None):
	cursor = database.cursor()
	answer = question.GetAnswer()
	content = question.GetQuestion()
	query = "INSERT INTO FillingQuestion (`Content`, `Answer`, `Solution_Id`, `Path_Id`) VALUES ('{0}', '{1}', {2}, {3});".format(content, answer, "NULL", path_id)
	ExecuteAlterCommand(database, cursor, query)
	return int(cursor.lastrowid)

# 插入填充題
def InsertSelectQuestion(database, question, path_id):
	cursor = database.cursor()
	answer = "1"
	content = question.GetQuestion()
	option_content = [question.GetOption(1).GetContent(), question.GetOption(2).GetContent(), question.GetOption(3).GetContent(), question.GetOption(4).GetContent()]
	query = "INSERT INTO SelectQuestion (`Content`, `Answer`, `Option1`, `Option2`, `Option3`, `Option4`, `Path_Id`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6})".format(content, answer, option_content[0], option_content[1], option_content[2], option_content[3], path_id)
	ExecuteAlterCommand(database, cursor, query)
	return int(cursor.lastrowid)

# 插入圖片 (yet not test)
def InsertImage(database, q_id, source, image_blob):
	cursor = database.cursor()
	# 先插入一個空的
	ExecuteAlterCommand(database, cursor, "INSERT INTO `Image` (`Question_Id`, `Source`) VALUES ({0}, '{1}');".format(q_id, source))
	id = int(cursor.lastrowid) 
	# 在更新他
	UpdateImage(database, id, image_blob)

# 更新圖片
def UpdateImage(database, id, image_blob):
	cursor = database.cursor()
	handler = database.cursor()
	ExecuteAlterCommand(database, cursor, "UPDATE `Image` SET `Image`=%s WHERE `Id`=%s", (image_blob, id))

# 以id 搜尋圖片 (return bytes)
def SearchImageById(database, id):
	handler = database.cursor()
	query = "SELECT `Image` FROM `Image` WHERE `Id`={0}".format(id)
	handler.execute(query)
	result = handler.fetchone()[0]
	return result

# 以Question的id 以及 Source 搜尋圖片 (return list for (id, image))
def SearchImageByQuestion(database, q_id, source):
	handler = database.cursor()
	query = "SELECT `Id`, `Image` FROM `Image` WHERE `Question_Id`={0} and `Source`='{1}';".format(q_id, source)
	handler.execute(query)
	result = handler.fetchall()
	return result

# 以id 刪除圖片 (return list for (id, image))
def DeleteImageById(database, image_id):
	cursor = database.cursor()
	query = "DELETE FROM `Image` WHERE `Id`={0};".format(image_id)
	ExecuteAlterCommand(database, cursor, query)

# 從Table中得到id
def GetIdFromTable(database, table, name):
	handler = database.cursor()
	query = "SELECT `Id` FROM {0} WHERE `Name`='{1}'".format(table, name)
	handler.execute(query)
	try:
		return int(handler.fetchone()[0])
	except:
		return None

# 得到subject 的id (如果不存在 返回False)
def GetSubjectId(database, subject_name):
	return GetIdFromTable(database, "Subject", subject_name)

# 得到level1 的id (如果不存在 返回False)
def GetLevel1Id(database, level1_name):
	return GetIdFromTable(database, "Level1", level1_name)

# 得到level2 的id (如果不存在 返回False)
def GetLevel2Id(database, level2_name):
	return GetIdFromTable(database, "Level2", level2_name)

# 更新 Subject 的名字
def UpdateLevel1Name(database, id, subject):
	cursor = database.cursor()
	query = "UPDATE Subject SET `Name`='{0}' WHERE Id={1};".format(subject, id)
	ExecuteAlterCommand(database, cursor, query)

# 更新 Level1 的名字
def UpdateLevel1Name(database, id, level1_name):
	query = "UPDATE Level1 SET `Name`='{0}' WHERE Id={1};".format(level1_name, id)
	ExecuteAlterCommand(database, cursor, query)

# 更新 Level2 的名字
def UpdateLevel2Name(database, id, level2_name):
	query = "UPDATE Level2 SET `Name`='{0}' WHERE Id={1};".format(level2_name, id)
	ExecuteAlterCommand(database, cursor, query)

# 更新 填充題
def UpdateFillingQuestion(database, question):
	cursor = database.cursor()
	content = question.GetQuestion()
	answer = question.GetAnswer()
	query = "UPDATE FillingQuestion SET `Content`='{0}', `Answer`='{1}' WHERE `Id`={2};".format(content, answer, question.id)
	ExecuteAlterCommand(database, cursor, query)

# 得到所有路徑 (return list[str])
def GetTotalPath(database):
	handler = database.cursor()
	pre_query = "SELECT Subject.Name, Level1.Name, Level2.Name FROM Subject, Level1, Level2 NATURAL JOIN PathTable "
	condition1 = "WHERE (Subject.Id=PathTable.Subject_Id and Level1.Id=PathTable.Level1_Id and Level2.Id=PathTable.Level2_Id)"
	query = pre_query + condition1
	handler.execute(query)
	path = [list(p) for p in handler.fetchall()]
	return path

# 搜尋路徑的Id (return list)
def SearchPathId(database, question_level=[[]]):
	# SELECT PathTable.Id, Subject.Name, Level1.Name, Level2.Name
	# FROM Subject, Level1, Level2
	# NATURAL JOIN PathTable
	# WHERE (Subject.Id=PathTable.Subject_Id and Level1.Id=PathTable.Level1_Id and Level2.Id=PathTable.Level2_Id) and ((Subject.Name="數學" and Level1.Name="盈虧問題" and Level2.Name="基本型") or (Subject.Name="數學" and Level1.Name="盈虧問題" and Level2.Name="份數轉化"))
	if MyLibrary.CheckListDimension(question_level) == 1:
		question_level = [question_level]
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
	count = 1
	for data in result:
		qList.append(MyLibrary.Question(data[0], data[2], qnumber=count))
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