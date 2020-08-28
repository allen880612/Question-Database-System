import os
def OpenWord():
	print(os.getcwd())
	full_cmd = "answer.docx"
	os.popen("cd word" + " && " + full_cmd)

if __name__ == "__main__":
	OpenWord()