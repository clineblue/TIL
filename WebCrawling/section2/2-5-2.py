import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 사용하기 위해선 html 있어야 됨

html = """
<html>
<body>
<h1> 파이썬 BeautifulSoup 공부 </h1>
<p> 태그 선택자 </p>
<p> css 선택자 </p>
</body>
</head>
"""
# 하나의 html 이라고 가정

soup = BeautifulSoup(html, 'html.parser')
#명시적으로 파서를 지정. 이 내용이 객체로 만들어져서 soup에 할당이 되었다는거
print('soup', type(soup))
#soup <class 'bs4.BeautifulSoup'>
print('prettify', soup.prettify())
# prettify : html을 줄바꿈으로 보기 편하게 출력

h1 = soup.html.body.h1
# .을 찍으면서 접근할 수 있다.
#print('h1', h1)
# h1 만 가져옴 근데 그 안에 스트림, 즉 문자열만 가져온 건 아님

#print('h1', h1.string)
#문자를 가져오겠다.

p1 = soup.html.body.p
print('p1', p1)
# 1번째꺼 가져오, 형째 노드의 앞과 뒤를 구분해서 가져올 수 있지
#p가 같은 노드(레벨)에 2개. 어떤 걸 가져와야 되는가
p2 = p1.next_sibling.next_sibling
print('p2', p2)
#못가져올땐 줄바꿈으로 간거라서 나오지 않지. 따라서 2번
p3 = p1.previous_sibling.previous_sibling
print('p3', p3)
#이것도 줄바꿈으로 인해 2번 이동해줘야

print('h1>>', h1.string)
print('p2>>', p2.string)
print('p3>>', p3.string)

# 형제 노드를 2가지 메소드로 접근할 수 있다.
# 하지만 주로 쓰진 않지. html의 디자인의 변경이 되니까. 비효율적
