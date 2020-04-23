import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#태그 선택자를 활용해서 가져오기

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

#연속 파싱, 출력
# 보통 많이 사용하는 태그 선택자

links = soup.find_all("a")
# 한번에 가져옴, 인자로 태그를 받음
#print('links', type(links))

a = soup.find_all("a",string="daum")  #태그 이름과 속성 값을 같이 줌
print('a', a)
# '다음'만 가져온다
b = soup.find("a")
print('b', b)
#맨 위에 하나만 가져오겠지
c = soup.find_all(string=["naver", "google"]) #태그 이름 없이 속성 값만을
print('c', c)
# 있으면 반환하는건데 정규표현식을 써서 어떤 문자로 시작되거나 할때 불러올때


for a in links:
    href = a.attrs["href"] #a의 속성값 즉, 링크
    txt = a.string #a의 문자열
    print('txt >> ', txt, 'href >> ', href)
