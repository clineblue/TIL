import sys
import io
from bs4 import BeautifulSoup
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.daum.net/"
res = req.urlopen(url).read() # response 받기
soup = BeautifulSoup(res, "html-parser") # 파싱

# print('soup', soup.prettify()) # 다음에서 받아오는지, prettify - 깔끔

top = soup.select("ul#topMyListNo1 > li")
# > == 자식
print(top)

for e in top:
    print('e>>>', type(e))
# result = class. bs4.element.Tag  // 정확하게 인스턴트 형태이기에 때문에 끝난게 아니다

for e in top:
    print('e>>>', e.find("a").string)
# a태그의 문자열만 가져오겠다. 그럼 순서대로 쭉 나오겠지

for i,e in enumerate(top,1):
    print(i,",",e.find("a").string)
#enumberate함수를 사용하면 인덱스를 줄 수 있다. i값도 빠뜨리지 말 것!
#시작인덱스를 top,1로 주면 0부터 시작하지 않

for i, e in enumerate(top,1):
    print(i,",",e.find("a").string, " : ", e.find("span").string)
#ex  1 , 삼성전자 : 2,442,008
