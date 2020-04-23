import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1269/1269349/e4ce4a62256bf7c1bce8_20200414115323397.jpg"
imglUrl2 = "https://ssl.pstatic.net/tveta/libs/1223/1223689/b13e352ebd9aaebf2116_20200217145745541.png"
savePath1 = "/Users/kim/Desktop/test1.jpg"
savePath2 = "/Users/kim/Desktop/test2.jpg"

data = dw.urlopen(imgUrl).read()
data2 = dw.urlopen(imglUrl2).read()

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(data)

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(data2)

print("다운로드 완료")




