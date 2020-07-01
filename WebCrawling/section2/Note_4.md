2-7-4
---
---
* 과제 : 네이버 핫토픽 제목과 링크 스크랩핑
* 코드 작성은 전에 배운걸 그대로 작성해서 쉬웠지만, 제목이 2개씩 나오는 걸 확인했다. 원인을 알아보니 li > div에서 class가 2개(roll_next, roll_cur)가 있고, 각각 자식은 동일한 클래스의 이름으로 설정되어있었다. 그러다보니 맨 아래단의 클래스 이름만으로 간단하게 스크랩핑을 하니까. next클래스에서 텍스트 1개, cur클래스에서 1개 총 2개를 가져오는 것이다. 따라서 첫 번째 클래스만 가져오게끔 설정하였다
* 하이퍼링크 출력하는 법
  * e['href'] 
2-8-1
---
---

1. 브라우저 상 이미지 src
   * <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5191%2F2016%2F06%2F10%2F33ed99c856f314e91e0deeaeb99b6738_99_20160610141205.jpg&amp;type=b400" 
2. select 함수를 통한 선택자 파싱을 끝내고 출력 후 
   * src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
   * data-source="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODA4MDlfMjE5%2FMDAxNTMzODIzNDM2MzI1.6fs6GtL-7pcusb3vmxbyCiWkaWSgpN2TvjROEZ1RJZog.QAJOsdBqDi8XFqSRAthSRcDS0ZorlnotNkzAEGbKKtEg.JPEG.kled123%2FDiOBiJVVMAAMcIU.jpg&amp;type=b400"

브라우저 상 이미지 src가 base 64형식의 스트링값으로 변환되어 나옴. 이는 브라우저를 통해 접속한게 아닌 http 요청을 직접 날렸기 때문에 그런 것으로, data-source값으로 올바른 리턴이 이루어지는 것을 알 수 있음

* 아래 코드의 오류를 찾는다고 너무 많은 시간을 허비했다. 사실 os모듈의 함수는 처음이라 제대로 살펴보지 않고 강의만 듣고 따라했는데, 제대로 알지 못하면 정답을 알고 있어도, 내가 뭘 잘못했는지 찾기 어렵다. 여기서 문제는 .join함수는 폴더와 파일부분을 합쳐주는 것인데, 그 구분을 쉼표(,)로 해주는데도 불구하고, 나는 3가지 구분(폴더, 파일, 파일의 형식)을 해버린 것이다. 사실 2가지 구분(폴더,파일)만 해야하는데. 

  ```python
  fileName = os.path.join(savePath, savePath+str(i),'.jpg')
  #잘못된 코드
  fileName = os.path.join(savePath, savePath+str(i)+'.jpg')
  #정확한 코드
  ```
파일 생성 코드의 2가지 방식
---

---

```python
#1번째 방식
try:
    if not (os.path.exists(savePath)):
        os.makedirs(savePath)
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory")
        raise
#2번째 방식        
try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!")
        raise
```
os 모듈
---
---
os.makedirs(*name*, *mode=0o777*, *exist_ok=False*)

재귀적 디렉터리 생성 함수. [`mkdir()`](https://docs.python.org/ko/3/library/os.html#os.mkdir)와 비슷하지만, 말단 디렉터리를 포함하는 데 필요한 모든 중간 수준 디렉터리들을 만듭니다.

*mode* 매개 변수는 말단 디렉터리를 만들기 위해 [`mkdir()`](https://docs.python.org/ko/3/library/os.html#os.mkdir)로 전달됩니다; 이것이 어떻게 해석되는지는 [mkdir() 설명](https://docs.python.org/ko/3/library/os.html#mkdir-modebits)을 보십시오. 새로 만들어지는 부모 디렉터리들의 파일 권한 비트를 설정하려면, [`makedirs()`](https://docs.python.org/ko/3/library/os.html#os.makedirs)를 호출하기 전에 umask를 설정할 수 있습니다. 이미 존재하는 부모 디렉터리의 파일 권한 비트는 변경되지 않습니다.

*exist_ok* 가 `False`(기본값)면, 대상 디렉터리가 이미 있을 때 [`FileExistsError`](https://docs.python.org/ko/3/library/exceptions.html#FileExistsError)가 발생합니다.

---
여러 줄 주석 : '''  ''' , """  """"
파이참 여러 줄 주석 command + /



파일 읽기, 쓰기
---

---

#### 파일 모드

* R : 기존 파일 읽기
* W : 기존 파일 내용 제거하고, 처음부터 쓰기
* A : 기존 파일에 내용 추가하기
* t(text) : 자동 인코딩/디코딩 모드

#### 파일 객체의 주요 멤버 함수

* write() : 파일에 쓰기
* read() : 파일 읽기
* close() : 파일 닫기

* open('filePath.txt', 'rt', encoding = 'utf-8')
  * rt를 사용할 때 인코딩 지정해주면 편함

#### With절

~~~python
    with open(savePath+"title_"+str(i)+".txt","wt") as f:
         f.write(e.select_one("div.card-content > div.course_title").string)
~~~

* with 절을 사용하면 f.close() 클로즈 함수를 사용해줄 필요가 없음
* 파이썬은 소스코드를 실행하기 전에, 소스파일의 내용을 먼저 디코딩합니다. 소스코드 인코딩을 파이썬에게 잘못 알려주면, SyntaxError 예외가 발생합니다. 주석이라도 예외가 발생.