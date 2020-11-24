#coding:utf-8

#import win32clipboard as w
#import win32con

#　獲取複製的文字，不過QT 好像有自己的 QClipBoard，反正目前除了圖片暫時用不道

#def GetCopyBoard():
#    w.OpenClipboard()
#    copyTextBytes = w.GetClipboardData(win32con.CF_TEXT)
#    w.CloseClipboard()

#    copyText = copyTextBytes.decode('UTF-8')
#    return copyText

#print (GetCopyBoard())

from PIL import ImageGrab
from PIL import Image
import io

# 不確定存出來 是不是就是 BLOB 吃的格式
# 不是的話 就存成QDSTempImage 拿比較保險
def ConvertImageToByteArray(image:Image):
  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format=image.format)
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr

img = ImageGrab.grabclipboard()
#im.save('somefile.png','PNG')
#print ( ConvertImageToByteArray( img ) )
if img:
	img.show()

# 轉成 QPixmap
from PIL.ImageQt import ImageQt

qim = ImageQt(im)
pix = QPixmap.fromImage(qim)