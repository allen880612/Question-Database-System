import pymysql as mysql
# 科目 類型 題型 兩個問題 圖片 大概6個Table

# 插入一個科目
def InsertSubject(database, subject_name):
	handler = database.cursor()
	query = "INSERT INTO Subject VALUES ('{0}');".format(subject_name)
	handler.execute(query)

# 插入一個Level1 (etc 盈虧問題 燕尾定理)
def InsertLevel1(database, level1_name):
	handler = database.cursor()
	query = "INSERT INTO Level1 VALUES ('{0}');".format(level1_name)
	handler.execute(query)

# 插入一個Level2 (etc 基本型 倍數轉化)
def InsertLevel2(database, level2_name):
	handler = database.cursor()
	query = "INSERT INTO Level2 VALUES ('{0}');".format(level2_name)
	handler.execute(query)