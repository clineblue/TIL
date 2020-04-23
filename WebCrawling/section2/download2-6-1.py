import sys
import io
from bs4 import BeautifulSoup
import re #regex = regular express

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html><body>
  <ul>
    <li><a id="naver" href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""


soup = BeautifulSoup(html,'html.parser')
print(soup.find(id="naver"))
li = soup.find_all(href=re.compile(r"^https://"))
# 정규표현식 - 거의 사용 안함
for i in li:
    print(i.attrs['href'])
    #attrs 속상값만을 출력

