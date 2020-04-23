import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# css 선택자 // 스크랩핑에 가장 많이 쓰임
# naming 으로 가져오기 때문에. id 값이 잘 안바뀜
html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select_one("div#main > h1")
print('h1', h1.string)


list_li = soup.select("div#main > ul.lecs > li")
for i in list_li:
    print(i.string)
# no attribute 속성이 없다.>> 얘 타임은 list임
# 하나인 경우에도 반복문을 돌려야 됨
