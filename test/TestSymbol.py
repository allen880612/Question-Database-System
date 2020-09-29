from sympy import *
from docx import Document
from lxml import etree

# create expression
x, y = symbols('x y')
#expr1 = (x+y)**2
expr1 = x/y

from sympy.parsing.latex import parse_latex
#expr1 = parse_latex(r"\overline{a}")
expr1 = parse_latex(r"\frac {1 + \sqrt {\a}} {\b}")

#expr1 = symbols('\overline{AB}')

# create MathML structure
expr1xml = mathml(expr1, printer = 'presentation')
tree = etree.fromstring('<math xmlns="http://www.w3.org/1998/Math/MathML">'+expr1xml+'</math>')

# convert to MS Office structure
xslt = etree.parse('MML2OMML.XSL')
transform = etree.XSLT(xslt)
new_dom = transform(tree)

# write to docx
document = Document()
p = document.add_paragraph("2 + ")
p._element.append(new_dom.getroot())
p.add_run(' = 2x')
document.save("simpleEq.docx")

