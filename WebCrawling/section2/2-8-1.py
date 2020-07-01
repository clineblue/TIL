#네이버 이미지 다운받기
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사나")
url = base + quote

res = req.urlopen(url)
savePath = "/Users/kim/Desktop/image/"

try:
    if not (os.path.exists(savePath)):
        os.makedirs(savePath)
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory")
        raise
# 폴더 생성
# try:
#     if not(os.path.isdir(savePath)):
#         os.makedirs(os.path.join(savePath))
# except OSError as e:
#     if e.errno != errno.EEXIST:
#         print("Failed to create directory!")
#         raise
# 폴더 생성.v2

soup = BeautifulSoup(res, "html.parser")
li_list = soup.select("div > a.thumb._thumb > img")
#print(soup)

for i, e in enumerate(li_list,1):
    fileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(e['data-source'], fileName)
#user-agent가 브라우저가 아니므로 img src가 아닌 data-source가 이미지의 출처로 나옴

print("다운로드 완료!")