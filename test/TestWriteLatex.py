import latex2mathml.converter
from docx import Document
from sympy.parsing.latex import parse_latex
from lxml import etree
from sympy import *


def GetMathEquationByXMLString( xml_string ):
	tree = etree.fromstring(xml_string)
	xslt = etree.parse('MML2OMML.XSL')	# 注意這個檔案是不是在預期路徑上
	transform = etree.XSLT(xslt)
	new_dom = transform(tree)
	return new_dom.getroot()


'''
Test Case
'''
def Test():
	d = Document()
	p = d.add_paragraph("")

	latex_string = '\mathrm{N}_{2(\mathrm{~g})}+3 \mathrm{H}_{2(\mathrm{~g})} \rightarrow 2 \mathrm{NH}_{3(\mathrm{~g})}'
	latex_string = input()
	#latex_string = '\mathrm{KClO}_{3(\mathrm{~s})} \frac{\mathrm{MnO}_{2}}{\triangle} \mathrm{KCl}_{(\mathrm{s})}+\mathrm{O}_{2(\mathrm{~g})}'
	mathml_output = latex2mathml.converter.convert(latex_string)
	print (mathml_output)
	p._element.append( GetMathEquationByXMLString(mathml_output) )
	
	d.save("WriteLatex.docx")

if __name__ == '__main__':
	Test()