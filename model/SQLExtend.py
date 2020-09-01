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

# 插入選擇題
def InsertSelectQuestion(database, question, path_id):
	cursor = database.cursor()
	answer = " ".join(question.GetAnswer())
	content = question.GetQuestion()
	option_content = GetSelectOptionContent(question)
	print(option_content)
	#print("option: " + " ".join(option_content))
	#query = "INSERT INTO SelectQuestion (`Content`, `Answer`, `Option1`, `Option2`, `Option3`, `Option4`, `Option5`, `Option6`, `Option7`, `Option8`, `Path_Id`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', {10});".format(content, answer, option_content[0], option_content[1], option_content[2], option_content[3], option_content[4], option_content[5], option_content[6], option_content[7], path_id)
	query = "INSERT INTO SelectQuestion (`Content`, `Answer`, `Option1`, `Option2`, `Option3`, `Option4`, `Option5`, `Option6`, `Option7`, `Option8`, `Path_Id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
	parement = (content, answer, option_content[0], option_content[1], option_content[2], option_content[3], option_content[4], option_content[5], option_content[6], option_content[7], path_id)
	ExecuteAlterCommand(database, cursor, query, parement)
	return int(cursor.lastrowid)

# 插入圖片 (yet not test)
def InsertImage(database, q_id, source, image_blob):
	cursor = database.cursor()
	# 先插入一個空的
	ExecuteAlterCommand(database, cursor, "INSERT INTO `Image` (`Question_Id`, `Source`) VALUES ({0}, '{1}');".format(q_id, source))
	id = int(cursor.lastrowid) 
	# 在更新他
	UpdateImage(database, id, image_blob)

# 插入詳解
def InsertSolution(database, q_id, source, solution):
	cursor = database.cursor()
	content = solution.GetContent()
	query = "INSERT INTO `Solution` (`Question_Id`, `Source`, `Content`) VALUES (%s, %s, %s);"
	ExecuteAlterCommand(database, cursor, query, (q_id, source, content))
	return int(cursor.lastrowid)

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

# 搜尋選擇題中出現的所有圖片 (含選項)
def SearchImageBySelectQuestion(database, q_id):
	handler = database.cursor()
	s = ["SelectQuestion", "Option1", "Option2", "Option3", "Option4", "Option5", "Option6", "Option7", "Option8"]
	query = "SELECT `Id`, `Source`, `Image` FROM `Image` WHERE `Question_Id`={0} and (`Source`='{1}' or `Source`='{2}' or `Source`='{3}' or `Source`='{4}' or `Source`='{5}' or `Source`='{6}' or `Source`='{7}' or `Source`='{8}' or `Source`='{9}');".format(q_id, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8])
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

# 更新 選擇題
def UpdateSelectQuestion(database, question):
	cursor = database.cursor()
	q_content = question.GetQuestion()
	q_answer = " ".join(question.GetAnswer())
	print(len(question.option))
	option_content = GetSelectOptionContent(question)
	print(option_content)
	q_id = question.id
	#query = "UPDATE SelectQuestion SET `Content`='{0}', `Answer`='{1}', `Option1`='{2}', `Option2`='{3}', `Option3`='{4}', `Option4`='{5}', `Option5`='{6}', `Option6`='{7}', `Option7`='{8}', `Option8`='{9}' WHERE `Id`={10};".format(q_content, q_answer, option_content[0], option_content[1], option_content[2], option_content[3], option_content[4], option_content[5], option_content[6], option_content[7], q_id)
	query = "UPDATE SelectQuestion SET `Content`=%s, `Answer`=%s, `Option1`=%s, `Option2`=%s, `Option3`=%s, `Option4`=%s, `Option5`=%s, `Option6`=%s, `Option7`=%s, `Option8`=%s WHERE `Id`=%s;"
	parement = (q_content, q_answer, option_content[0], option_content[1], option_content[2], option_content[3], option_content[4], option_content[5], option_content[6], option_content[7], q_id)
	ExecuteAlterCommand(database, cursor, query, parement)

# 更新詳解
def UpdateSolution(database, q_id, source, solution):
	cursor = database.cursor()
	content = solution.GetContent()
	query = "UPDATE Solution SET `Content`='{0}' WHERE `Question_Id`={1} and `Source`='{2}'".format(content, q_id, source)
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

# 查詢詳解 (return QDS Solution)
def SearchSolution(database, q_id, source):
	cursor = database.cursor()
	query = "SELECT `Id`, `Content` FROM Solution WHERE `Question_Id`={0} and `Source`='{1}';".format(q_id, source)
	cursor.execute(query)
	data = cursor.fetchone()
	if data is None:
		return None

	# (id, Content)
	solution = MyLibrary.QDSSolution(int(data[0]), data[1])
	image_result = SearchImageByQuestion(database, q_id, solution.GetType())
	image_list = []
	for data in image_result:
		image_id = int(data[0])
		image_content = data[1]
		image_list.append(MyLibrary.QDSTempImage(image_content, image_id, isOnServer=True, isUpdated=False))

	solution.SetImages(image_list)
	return solution

# 以路徑搜尋Question (return Question List) (目前只搜尋填充題)
def SearchQuestionByPath(database, path_id):
	handler = database.cursor()
	query = "SELECT * FROM FillingQuestion WHERE FillingQuestion.Path_Id={0};".format(str(path_id))
	handler.execute(query)
	result = handler.fetchall()
	qList = []
	count = 1
	for data in result:
		q_id = data[0]
		q_source = "FillingQuestion"
		q_content = data[2]
		# 建立題目圖片
		images = SearchImageByQuestion(database, q_id, q_source) # 搜尋圖片 -> (id, image) <- 這句跑得有點慢 優化沒做好
		image_list = []
		for qds_temp_image in images:
			image_id = qds_temp_image[0]
			image_content = qds_temp_image[1]
			image_list.append(MyLibrary.QDSTempImage(image_content, image_id, isOnServer=True, isUpdated=False))

		# 查詢詳解
		solution = SearchSolution(database, q_id, q_source)
		# 新增進題目List
		newQuestion = MyLibrary.Question(q_id, q_content, qnumber=count, images=image_list)
		newQuestion.SetSolution(solution)
		qList.append(newQuestion)
		count+=1

	return qList

# 以路徑搜尋Question (return Question List) (搜尋選擇題)
def SearchSelectQuestionByPath(database, path_id):
	handler = database.cursor()
	query = "SELECT * FROM SelectQuestion WHERE SelectQuestion.Path_Id={0};".format(str(path_id))
	handler.execute(query)
	result = handler.fetchall()
	qList = []
	count = 1
	for data in result:
		q_id = data[0]
		q_source = "SelectQuestion"
		q_content = data[1]
		q_answer = data[2].split(' ')
		q_option_content = [data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]]
		select_question_images = SearchImageBySelectQuestion(database, q_id) # (id, source, images)
		imageList = [ [], [], [], [], [], [], [], [], [] ] # 9個
		for image in select_question_images:
			image_id, source, image_content = image[0], image[1], image[2]
			temp_image = MyLibrary.QDSTempImage(image_content, image_id, isOnServer=True, isUpdated=False)
			if source == "SelectQuestion":
				imageList[0].append(temp_image)
			elif source == "Option1":
				imageList[1].append(temp_image)
			elif source == "Option2":
				imageList[2].append(temp_image)
			elif source == "Option3":
				imageList[3].append(temp_image)
			elif source == "Option4":
				imageList[4].append(temp_image)
			elif source == "Option5":
				imageList[5].append(temp_image)
			elif source == "Option6":
				imageList[6].append(temp_image)
			elif source == "Option7":
				imageList[7].append(temp_image)
			elif source == "Option8":
				imageList[8].append(temp_image)

		# 建立選擇題
		select_question = MyLibrary.SelectQuestion(q_id, q_content, images=imageList[0], isUpdate=False)
		select_question.answer = q_answer
		for count in range(0, 8):
			index = count + 1
			if q_option_content[count] is not None:
				select_question.option.append(MyLibrary.SelectOption(index, q_option_content[count], imageList[index]))
		#select_question.option.append(MyLibrary.SelectOption(1, q_option_content[0], imageList[1]))
		#select_question.option.append(MyLibrary.SelectOption(2, q_option_content[1], imageList[2]))
		#select_question.option.append(MyLibrary.SelectOption(3, q_option_content[2], imageList[3]))
		#select_question.option.append(MyLibrary.SelectOption(4, q_option_content[3], imageList[4]))
		#select_question.option.append(MyLibrary.SelectOption(5, q_option_content[4], imageList[5]))
		#select_question.option.append(MyLibrary.SelectOption(6, q_option_content[5], imageList[6]))
		#select_question.option.append(MyLibrary.SelectOption(7, q_option_content[6], imageList[7]))
		#select_question.option.append(MyLibrary.SelectOption(8, q_option_content[7], imageList[8]))
		solution = SearchSolution(database, q_id, q_source)
		select_question.SetSolution(solution)
		qList.append(select_question)

		print(q_answer)
		content = [opt.GetContent() for opt in select_question.option]
		print(content)
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

##############################
def GetSelectOptionContent(question):
	return [question.option[i].GetContent() if i < len(question.option) else None for i in range(0, 8)]
