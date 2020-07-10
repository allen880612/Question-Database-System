import docx
import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
 
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

if __name__ == '__main__':
	test3()