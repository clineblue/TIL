#인프런 강좌 이미지 파일,텍스트 파일(제목) 다운
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/courses/it-programming/web-dev"

res = req.urlopen(url).read()
savePath = "/Users/kim/Desktop/image2/"

try:
    if not os.path.exists(savePath):
        os.makedirs(savePath)
except OSError as e:
    if e.errno != e.errno.EEXIST:
        print("ERROR!")
        raise

soup = BeautifulSoup(res,'html.parser')
#print(soup)
webClass = soup.select("a.course_card_front")
# 큰 뿌리를 잘 알아야 함. 공통된 곳까지 이곳에
#print(webClass)
for i,e in enumerate(webClass, 1):
    with open(savePath+"title_"+str(i)+".txt","wt") as f:
         f.write(e.select_one("div.card-content > div.course_title").string)
    fileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    req.urlretrieve(e.select_one("div.card-image > figure > img")['data-src'],fileName)

print("강좌 정보 텍스트 출력 및 이미지 다운 완료!")
