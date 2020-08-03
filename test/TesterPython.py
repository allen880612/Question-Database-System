import docx
import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

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

if __name__ == '__main__':
	#tc = testClass()
	#kk = test3(tc)
	#kk.append(456)
	#print(id(kk))
	#print(id(tc.tkList))
	test4()