"""
使用方法:

    -設定路徑- 請選擇一種設定(預設為1)
    -------------------------------------------
    1.  設工作路徑為本程式所在位置，
        把本程式放於word檔們所在位置即可直接使用
        
    2.  也可直接改最下方手動輸入的路徑，
        並解除該行註解
        
    -執行-
    -------------------------------------------
    執行將會把"同目錄"下的"docx"檔中的圖片，
    都轉為jpg檔 (doc檔不行，請先另存為docx)
    並存於以該word檔命名之資料夾下

"""

import os,zipfile,shutil
from PIL import Image
import glob

 
def getimage(docdir):
    print("Now working at : " + docdir)
    os.chdir(docdir)
    dirlist = os.listdir(docdir)
    for i in dirlist:
        if i.endswith(".docx"): #匹配docx文件
            docname = i.split(".") #以“.”做成列表形式
            os.rename(i,"%s.ZIP"%docname[0]) #重命名为ZIP格式
            f = zipfile.ZipFile("%s.ZIP"%docname[0], 'r')
            for file in f.namelist():
                if "word" in file:
                    f.extract(file)  #将压缩包里的word文件夹解压出来
            f.close()
            
            oldimagedir = r"%s\word\media"%docdir #定义图片文件夹
            imgDir = "%s\%s"%(docdir, docname[0])
            
            if os.path.isdir(imgDir): # 若之前做過的還存在
                shutil.rmtree(imgDir) #先將其移除
                
            shutil.copytree(oldimagedir, imgDir) #拷贝到新目录，名称为word文件的名字
            os.rename("%s.ZIP" % docname[0], "%s.docx"% docname[0]) #将ZIP名字还原为DOCX
            shutil.rmtree("%s\word"%docdir) #删除word文件夹

            #轉換圖片格式
            pic_dir = "%s\%s"%(docdir, docname[0])
            paths = glob.glob(os.path.join(pic_dir, "*.*"))
            
            for pic in paths:
                picformat = os.path.splitext(pic)[1] # get format name
                if picformat != ".jpg": # checking image wether to covert
                    img = Image.open(pic)
                    img =  img.convert('RGB')
                    savePath = os.path.splitext(pic)[0] + ".jpg" # name + format
                    print("orginal : " + pic)
                    print("covert : " + savePath)
                    print("----------------------------------------------")
                    img.save(savePath)
                    os.remove(pic) # delete orginal file
 
if __name__=="__main__":
    getimage(os.getcwd()) # 用腳本所在資料夾工作
    #getimage(r"G:\NTUT\TestWordWrite") # 手動輸入工作路徑 (請與上一行擇一使用)
