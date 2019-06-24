import os
import docx

#file = docx.Document("../database/d/chapter.docx")

path = "../database/基礎化學/下/"
print(os.listdir(path))

file = docx.Document("../database/選修化學/上/第二章 化學鍵結.docx")

for f in file.paragraphs:
    print(f.text)
