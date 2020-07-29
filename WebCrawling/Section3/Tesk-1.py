# 보안뉴스(긴급) 바탕화면 텍스트 저장

import sys
import io
import os
import requests
from bs4 import BeautifulSoup
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'http://www.boannews.com/media/news_rss.xml?skind=5'
savePath = "/Users/kim/Desktop/boanNews/"
res = req.urlopen(url)
with requests.Session() as s:
    r = requests.get(url)
    r.encoding = 'euc-kr'
    #print(r.text)

# 폴더만들기
try:
    if not os.path.exists(savePath):
        os.makedirs(savePath)
except OSError as e:
    if e.errno != e.errno.EEXIST:
        print("Error!")
        raise

# 선택자 접근
soup = BeautifulSoup(res, 'html.parser')
downLoad = soup.select('item')

for i,e in enumerate(downLoad, 1):
    with open(savePath+"뉴스"+str(i)+".txt", 'wt') as f:
        f.write(e.select_one('de:date').string)


print('완료')

