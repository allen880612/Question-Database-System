from docx import Document
import sys

document = Document()

# 傳入所在段落，與要上標處理的字串
def AddUpperWord( paragraph , upperText):
	upper_text = p.add_run( str(upperText) )
	upper_text.font.superscript = True

p = document.add_paragraph('X')
AddUpperWord(p, 2)

p.add_run(' + Y')
AddUpperWord(p, 2)
p.add_run(' = 214')

try:
	document.save('TestUpper.docx')
except:
	print (sys.exc_info()[0])
