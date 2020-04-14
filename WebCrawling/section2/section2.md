PackagesNotFoundError: The following packages are not available from current channels:
---

---

어제 python 3.4 버전을 설치하려 하는데 또, 채널 설정에 대한 에러가 뜬다. 어제 분명 채널을 설정해주었는데도 말이다. 
$ conda list 로 패키지를 확인해보았고, 혹시나 해서 
$ conda install -c conda-forge <package> 명령어를 사용, 설치해보려 했으나 이미 설치가 되어 있다고 했다. 
결국 python 3.7 버전으로 설치하고 생각해보니 python 3.7이 설치되어 있다고 해서 3.4. 버전이 설치되어있을거라 생각한게 좀 오류였던 것 같다.
최신 버전을 설치했다고 해서 과거의 버전들이 다 설치가 되어 있진 않을테니 말이다.



section 2 : 기초 스크랩핑 
---

---

한글 표시를 위한 utf-8 인코딩

~~~python
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
~~~



2-2-1
---

---

* urllib : URL 작업을 위한 여러 모듈을 모은 패키지
* urllib.request : URL 열고 읽기 위함 (간단하게 웹 페이지 요청 및 데이터를 가져올 수 있음)
  * urllib.request.urlopen("https://naver.com")
    * urlopen : 웹 페이지를 불러와, 리턴값으로 호출하여 얻은 데이터에 대한 객체를 반환
  * urllib.request.urlopen.read()
    * read 함수 : 실제로 결과를 출력
  * urllib.request.urlretrieve(접근url, 저장주소)
* urllib.error : urllib.request에서 발생하는 예외를 포함 하기 위함
* urllib.parse : URL 구문 분석(파싱)을 위함
* urllib.robotparser : robots.txt 파일을 구문 분석하기 위함



2-2-2
---

---

파일 생성하기

~~~python
f = open("newFile.txt", 'w')
data = 'hello World'
# or data = f.read()
f.write(data)
f.close()

# with as 구문
with open(savePath2, 'wb') as saveFile2:
      saveFile2.write(data2)
~~~

* open 함수 : <파일이름, 파일 열기 모드> 입력값(인자)으로 받고, 결과값으로 파일 객체를 돌려줌
* write 함수 : 파일 객체 f에 data를 씀
* read 함수 : 파일 내용 전체를 문자열로 돌려줌



2-3-1
---

---

~~~python
print(type(mem)) 
# type 을 알고 싶을 때 
print("geturl", mem.geturl())
# 요청했던 주소를 그대로 반환
print("status", mem.status)
# http 응답코드 http 200, 302, 403, 500 등 
print("headers", mem.getheaders())
# header를 반환
print("info", mem.info())
# info가 header보다 보기가 수월
print("code", mem.getcode())
# status와 유사
print("read", mem.read(50).decode("utf-8"))
# read(숫자) 해당 숫자만큼만 출력
~~~

~~~python
print(urlparse("http://www.encar.com"))
> ParseResult(scheme='http', netloc='www.encar.com', path='', params='', query='', fragment='')
~~~



2-3-2
---

---

하고자 하는 것 : http get 방식으로 API를 제공하는 사이트에서 request해서 그 결과값을 출력



url 뒤 파라미터 형식으로 변환해주는 작업

```python
from urllib.parse import urlencode
params = urlencode(values)

```

urlopen으로 http 요청을 보내고,이걸 읽어오고,decode까지 

```python
reqData = req.urlopen(url).read().decode('utf-8')
```



행정안전부 - 뉴스 소식 - 알립니다에서 제공하는 RSS주소를 이용하여 해당 내용 출력하는 과정.

API에서 파라미터(?) 뒷 숫자만 변경하면 다른 게시판으로 이동가능 

```python
API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values = {
    'ctxCd' : '1001'
}
```



JSON(JavaScript Object Notation)
---

---

* 데이터를 저장하거나 전송할 때 많이 사용되는 경량의 DATA 교환방식 (단순한 데이터 포맷 형태)
* 최근에는 XML을 대체해서 데이터 전송 등에 많이 사용된다

urlretrieve vs urlopen
---

---

urlretrieve : 파싱이 필요 없는 데이터 (바로 저장)

urlopen : 파싱이 필요한 데이터 ( 변수에 할당 ) 저장시 read() 필요

anaconda 가상환경에서 atom 실행이 안되는 현상 (mac os x)
---

---

터미널에서 anaconda 가상환경으로 접속 후 atom을 실행해보려 했으나, 가상환경으로 실행이 되지 않고, untitled로 일반적 atom이 실행되는 문제. 이에 anaconda상에서 atom 환경변수 경로설정이 제대로 되어 있지 않아 문제가 발생한 것으로 판단해서 bin_profile 파일을 들어가 수정해보려 했으나, 아래와 같이 경로는 제대로 잡혀있는 것으로 확인.
문제를 모르겠음. 그래서 파이참으로 아나콘다 가상환경에서 작업할 필요가 있다고 생각하여 파이참으로 연동하여 작업