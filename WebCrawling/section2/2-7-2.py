import sys
import io
from bs4 import BeautifulSoup
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/"
res = req.urlopen(url).read() # response 받기
soup = BeautifulSoup(res, "html-parser") # 파싱

top10 = soup.select("#siselist_tab_0 > tr")

for e in top10:
    print(e.find("a"))
# a태그가 없으면 none으로 반환값

i = 1
for e in top10:
    if e.find("a") is not None: # is not None = None값이 아니면 print
        print(i, e.select_one(".tltle".string))
        i += 1

