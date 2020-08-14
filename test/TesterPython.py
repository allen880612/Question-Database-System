import docx
import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
import pymysql as mysql
import threading
import time

class testClass():
	def __init__(self):
		self.tkList = [1, 2, 3]

def test1():
	tList = [1, 2, 3]
	print(tList)
	tList.remove(2)
	print(tList)

def test2():
	word = docx.Document()
	flag = True
	try:
		word.save("word/answer.docx")
	except:
		flag = False
	print(flag)
	return flag

def test3(tc):
	return tc.tkList

def test4():
	kkk = [1,2,3,4]
	print(kkk)
	kkk += [9,8,7,6]
	print(kkk)

def test5():
	t = threading.Thread(target = test5_subthread)
	t.start()
	t.join()
	time.sleep(5)
	myDB = mysql.connect(host="35.194.198.56",port=3306,user="root",passwd="zzxcv1234")
	cHandler = myDB.cursor()
	query = "SHOW DATABASES;"
	cHandler.execute(query)
	result = cHandler.fetchall()

	for row in result:
		print (row)

def test5_subthread():
	exe_name = "cloud_sql_proxy.exe"
	sql_id = "psyched-circuit-286314:asia-east1:xtest00=tcp:3306"
	key_name = "qds_key.json"
	cmd1 = "-instances=" + sql_id
	cmd2 = "-credential_file=" + key_name
	full_cmd = exe_name + " " + cmd1 + " " + cmd2 + " "
	os.popen("cd proxy" + " && " + full_cmd)

def test6(subject_name):
	query = "INSERT INTO Subject VALUES ({0})".format(subject_name)
	print(query)

if __name__ == '__main__':
	#tc = testClass()
	#kk = test3(tc)
	#kk.append(456)
	#print(id(kk))
	#print(id(tc.tkList))
	test6("Math")