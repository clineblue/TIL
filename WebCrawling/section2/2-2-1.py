import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://shop1.phinf.naver.net/20200318_269/15845006823959Vrd0_JPEG/21860516940677921_22371427.jpg"
htmlUrl = "http://www.google.com"
savePath1 = "/Users/kim/Desktop/test1.jpg"
savePath2 = "/Users/kim/Desktop/index.html"
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)
print("다운로드 완료")
#
