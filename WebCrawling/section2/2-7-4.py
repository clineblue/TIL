#네이버 핫토픽 출력
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://search.naver.com/search.naver?where=nexearch&query=%EC%97%89%EB%8D%A9%EC%9D%B4%20%EA%B1%B7%EA%B8%B0&sm=top_lve.ag20sgr0mamsimenmspm&ie=utf8"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")
RealimeSrch = soup.select("div.rank_roll > div.roll._next > span > a")
# a태그, 문자태그의 공통적인 부분까지만 적고 나머지는 밑에서 구현
for i,e in enumerate(RealimeSrch, 1):
    print(i,">>>",e.select_one("span.tit._text").string)
    print("link>>>", e['href']) #하이퍼링크 출력 방법




