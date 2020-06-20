2-7-1 / 2-7-1.new
---

---

다음 금융 시가총액 상위 10
ajax 방식으로 변경되어 기존의 코드 사용되지 않음
흐름을 확실히 잡으면 그 이후도 수월

AJAX
----

---

Asynchronous Javascript And Xml(비동기식 자바스크립트와xml)
브라우저가 가지고있는 XMLHttpRequest 객체를 이용해서 전체 페이지를 새로 고치지 않고도 페이지의 일부만을 위한 데이터를 로드하는 기법 이며 Ajax를 한마디로 정의하자면 JavaScript를 사용한 비동기 통신, 클라이언트와 서버간에 XML 데이터를 주고받는 기술이라고 할 수 있겠습니다.

기본적으로 HTTP프로토콜은 클라이언트쪽에서 Request를 보내고 Server쪽에서 Response를 받으면 이어졌던 연결이 끊기게 되어있습니다. 그래서 화면의 내용을 갱신하기 위해서는 다시 request를 하고 response를 하면서 페이지 전체를 갱신하게 됩니다. 하지만 이렇게 할 경우 페이지의 일부분만 갱신할 경우에도 페이지 전체를 다시 로드해야하는데 엄청난 자원낭비와 시간낭비를 초래하고 말것입니다. 하지만 ajax는 html 페이지 전체가아닌 일부분만 갱신할수 있도록 XML HttpRequest객체를 통해 서버에 request를 합니다. 이 경우 Json이나xml형태로 필요한 데이터만 받아 갱신하기 때문에 그만큼의 자원과 시간을 아낄 수 있습니다. 요새 웹페이지에서 가장 중요한것은 속도가 아닐까싶습니다. 이 이유하나만으로도 Ajax를 사용해야 하는 이유로써 충분합니다.

요약 : 웹페이지 전체가 아닌 일부만의 데이터를 로드하기 위한 기술

JSON
---

---

JSON (JavaScript Object Notation)

경량의 DATA 교환 방식
javascript에서 객체를 만들 때 사용하는 표현식
최근엔 JSON이 XML을 대체해서 데이터 전송

User_Agent
---

---

1. 사용자를 대신해서 인터넷에 접속하는 소프트웨어, 즉 브라우저
2. 인터넷 사이트에 접속할 때 UA(UserAgent)는 사용자에 관한 정보를 헤더에 담아 전송하게 됨
3. 즉, UA는 접속한 브라우저 +OS정보
4. 현재 내 userAgent
   Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 RuxitSynthetic/1.0 v334910657 t18859



XHR(XMLHttpRequest)
---

---

1. AJAX 요청을 생성하는 JavaScript API

2. XHR의 메서드로 브라우저와 서버간의 네트워크 요청을 전송할 수 있음

Fake_useragent
---

---

웹 사이트는 내가 브라우저를 통해서 접근하는지, 파이썬을 통해서 접근하는지 알 수 있다. 따라서 파이썬(크롤링)으로 접근이 되지 않는다면 가상의 agent를 설정하여 접속해야한다

~~~python
pip install fake-useragent #cmd

import json
import urllib.request as req
from fake_useragent import UserAgent
us = UserAgent()

print(us.ie) 
#internet explore로 접속하는 것처럼 fake
print(us.msie) 
#모바일 internet explore로 접속하는 것처럼 fake
print(us.chrome)
#크롬로 접속하는 것처럼 fake
print(us.safari)
#사파리로 접속하는 것처럼 fake
print(us.random)
#랜덤


header = {'User-Agent':us.ie,
'referer':'https://finance.daum.net/'}
url = 'https://finance.daum.net/api/search/ranks?limit=10'
res = req.urlopen(req.Request(url,headers=header)).read().decode('utf-8')
a = json.loads(res)
a['data']
# [출처] [· Python 24일차 크롤링 fake-useragent](https://blog.naver.com/jjune0601/221881323184)|**작성자** [용돈천원](https://blog.naver.com/jjune0601)

import requests
from fake_useragent import UserAgent
#크롬 이용해 구글을 열면 크롬이 유저를 대신해서, 내 유저가 google을 열고 싶어한다고 구글 server에게
#대신 말해줌, 구글은 요청 받고 이거에 respone해준다. 근데 만약 코드나 로봇이 이걸요청한다는걸 서버가
# 알면 server는 반응을 안한다.(다그러는건 아니고 그런 사이트가 있음)
# 그렇기 때문에 로봇이나 코딩이 아니라고 속이기 위해 fake_useragent를 사용

# Background on user-agents(fake유저 만들기)

ua = UserAgent()

header = {'user-agent':ua.chrome} #header는 사전형=디렉토리형식이니까 header만들어 줌
#print(ua.chrome) => Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0
#chrome이 여는 어떤 사이트든 server에 request할때 보내는 header임

#구글에 요청 보내기(headers=header해주면, 내 header가 크롬이라는 걸 알려줌으로써 내가 code나 로봇이 아닌
#직접 누른 거라고 생각하게 fake치는 것, 구글은 code로 받아도 상관없어서 headers필요 없긴 함
page = requests.get('https://www.google.com',headers=header)
print(page.content)

# # Background on Timeout
# 로드 엄청느리거나 오류 생길때, 요청한 서버에서 process 오래걸리거나해서
# 반응을 제대로 주지 못하고 시간 무제한으로 걸릴때 있으니까, 이때 새로고침하게하는 기능
#timeout=3는 시간이 3이상 지나면 다시 요청해라
page = requests.get('https://www.google.com',timeout=3)
[출처] request-get method/fake_useragent|작성자 아아아



~~~



2-7-2 / 2-7-2.new
---

___

* 네이버 금융 상한가 top 10
  ajax 방식으로 변경되어 기존의 코드 사용되지 않음

* python의 비교문에는 ==(equal), !=(not equal) , not , is 가 있다.
* ==, is 는 같아보이지만 다르다. 
* ==는 데이터를 비교하지만  is는 데이터가 아닌 포인터(레퍼런스)를 비교하는 연산자이다. 따라서 is 커맨드는 상수(None, True, False)에만 쓰도록 하자.



파이썬 포맷팅
---

---

방법 2가지 

1. % 포맷팅
   * %연산자와 포맷 스트링을 사용하는 방법
   * 대표적 포맷 스트링 : %d, %s, %f

~~~python
print("integer : %d, string : %s, float : %f"%(10,"str",0.1))
~~~

2. format 포맷팅
   * {}를 이용한 포맷팅 방법으로 %와 동일한 기능 지원, 변수의 타입과 상관없이 괄호, 숫자만 이용

~~~python
print("integer : {}, string : {}, float : {}".format(10,"hi",0.1))
~~~

파이썬은 간단,명료하게 코드를 작성하는게 그 목적이므로 포맷팅 자체는 성능에 부하가 없기 때문에 코드 가독성이 좋은 format함수를 사용



2-7-3
---

___

* 인프런 웹 개발 강좌 페이지 제목 크롤링
* "추천-강좌" 페이지가 없어졌기 때문에 새로운 페이지에 선택자를 찾는다고 고생을 좀 했다. 이제 조금 어떻게 돌아가는지 알 것 같은데 아직 선택자를 찾고 선별하는 과정이 꽤나 어렵다. 오류도 많고. 



bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser. Do you need to install a parser library?
---

___

~~~python

soup = BeautifulSoup(res, "html.parser")
#정상 코드
soup = BeautifulSoup(res, "html-parser")
#오류 코드

~~~

해당 오류가 발생하면 pip install lxml을 사용하여 해결하라고 했는데, 실상은 아래 코드를 이렇게 작성한 것이다. 젠장. 이거가지고 대략 3시간은 헤매고 다녔다...



AttributeError: 'NoneType' object has no attribute 'string'
---

___

~~~python
print(i,e.select_one("div.course_title").string)
# 정상
print(i,e.select_one("course_title").string)
# 오류
~~~

정신차리자~!



