

urljoin
---

---

```python
from urllib.parse import urljoin

baseurl = "http://test.com/html/a.html"
print(">>", urljoin(baseurl, "b.html"))
# >> http://test.com/html/b.html
```

url 경로, 파일 변경시 사용

urljoin은 일정 경로까지는 확정, 밑 파일 변경가능

위 폴더까지 변경시 "../index.html" 와 같이 입력시 가능



* 생성자를 몰랐다. 
  인스턴스를 생성할 때 매개변수로 초기화 값을 넣어 주는 것. 그게 바로 생성자이다. 
  생성자는 인스턴스 변수(필드 값 등)를 초기화 시키는 역할



Beautiful Soup란?
---

---

HTML 및 XML 파일에서 원하는 데이터를 손쉽게 Parsing 할 수 있는 Python 라이브러리 입니다.

파이썬으로 웹을 크롤링 한 후 HTML 태그로 부터 원하는 데이터를 가져올 때, 파싱하기 편하게 해주는 라이브러리이다.

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
```



prettify /
---

previous_sibling / next_sibling
---

---

prettify : html을 줄바꿈으로 보기 편하게 출력

previous_sibling / next_sibling : 이전, 다음 태그에 대한 접근

잘 사용하지 않음, html의 디자인은 계속 변경되니까.

```python
html = """
<html>
<body>
<h1> 파이썬 BeautifulSoup 공부 </h1>
<p> 태그 선택자 </p>
<p> css 선택자 </p>
</body>
</head>
"""

print('prettify', soup.prettify())

h1 = soup.html.body.h1
print(h1)
# .으로 접근가능 하지만 스트림만 가져온 건 아님

print('h1', h1.string)
#문자만 가져오겠다.

p1 = soup.html.body.p
print('p1', p1)
# 첫 번째 p태그만

p2 = p1.next_sibling.next_sibling
print('p2', p2)
# 1번만 적용시, 줄 바꿈으로 인해 출력 오류. 따라서 2번 적용시켜줘야 제대로 출력 됨간거라서 나오지 않지. 따라서 2번

p3 = p1.previous_sibling.previous_sibling
print('p3', p3)
```



soup.find / soup.find_all
---

---

태그 또는 속성값으로 찾기 / 전부 찾기 (html)

- find_all(name, attrs, recursive, string, limit, **kwargs)
- find(name, attrs, recursive, string, **kwargs)



```python
a = soup.find_all("a",string="daum")  
print('a', a)
# 태그 이름, 속성 값
b = soup.find("a")
print('b', b)
# 태그 이름 // 맨 위에 하나만
c = soup.find_all(string=["naver", "google"]) 
print('c', c)
# 속성 값

links = soup.find_all("a")
for a in links:
    href = a.attrs['href'] # a의 속성값 즉, 링크만
    txt = a.string # a의 문자열만
    print('txt >> ', txt, 'href >> ', href)
```



soup.select / soup.select_one
---

---

CSS선택자(naming)으로 파싱
id, class값은 잘 안 바뀌기에 스크래핑에 가장 많이 쓰임

```python
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
# select는 list type으로 반환하기 때문에 단 1개라도 반복문을 돌려야 한다.
```





* 공식문서 : https://www.crummy.com/software/BeautifulSoup/bs4/doc/#











