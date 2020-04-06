#  Git 초기 설정

---

## 1 Mac 터미널 설정

---

### 1.1 remote repository 만들기 

* Github 홈페이지

#  Git 초기 설정

---

## 1 Mac 터미널 설정

---

![스크린샷 2020-04-05 오전 12 23 09](https://user-images.githubusercontent.com/62727831/78518440-70221580-77fb-11ea-9991-27905d2c4492.png)

### 1.1 remote repository 만들기 

* Github 홈페이지

### 1.2 local repository 만들기 

* $ mkdir GitStart
  * 코딩할 폴더 만들기
* $ cd Gitstart

### 1.3 remote - local repo 연결 설정

* $ git config --global user.name "이름" 
  * git commit에 사용될 username
* $ git config --global user.email "가입한 email" 
  * git commit에 사용될 e-mail
* $ echo "GitStart" >> README.md
* echo 명령어는 새로운 파일(READMD라는 마크애니 문법파일), 그 파일의 내용을 생성(GitStart)
* $ git init
  * 로컬 저장소를 초기화 하는 명령어 즉, "여기가 로컬 저장소야"라고 알려주는 명령어
* $ git status 
  * local repository 상태 확인
* $ git add README.md 
  * 해당 파일 staged 상태로 만들기 or 깃 목록에 파일 추가
  * git add . > 디렉토리 내 모든 파일 올리기
* $ git commit -m "코멘트"
  * staged -> commited상태로 변환
  * local에 저장(커밋)
* $ git remote add origin https://주소
  * local과 remote repository 연결 설정
* $ git push -u origin master
  * local -> remote repository로 전송
  * remote repository에 master라는 branch를 생성
  
  ![스크린샷 2020-04-05 오전 12 23 18](https://user-images.githubusercontent.com/62727831/78518492-9a73d300-77fb-11ea-9817-d7825d4c400e.png)
  
  
  

## 2.2 파이참 설정

---

![스크린샷 2020-04-06 오후 12 27 23](https://user-images.githubusercontent.com/62727831/78521080-a794c000-7803-11ea-8638-ce3a998df803.png)
* open

![스크린샷 2020-04-06 오후 12 27 32](https://user-images.githubusercontent.com/62727831/78521085-ab284700-7803-11ea-80c8-8262b48f2844.png)

![스크린샷 2020-04-06 오후 12 27 48](https://user-images.githubusercontent.com/62727831/78521088-ae233780-7803-11ea-8caf-bc6c7d6784aa.png)

* 자신의 git hub URL 삽입
* 저는 이전에 미리 해봐서 아이디, 비밀번호 입력하는게 따로 없으나 URL 입력시 따로 입력하는 칸이 나오는데 입력하시면 됩니다.


![스크린샷 2020-04-06 오후 12 28 51](https://user-images.githubusercontent.com/62727831/78521125-d90d8b80-7803-11ea-9226-e99cf88adc4f.png)

*짜자잔

![스크린샷 2020-04-06 오후 12 28 51](https://user-images.githubusercontent.com/62727831/78521242-399cc880-7804-11ea-8e7e-73214db35e09.png)


![스크린샷 2020-04-06 오후 12 31 12](https://user-images.githubusercontent.com/62727831/78521260-45888a80-7804-11ea-9e58-8976d5c3db0e.png)

* commit


![스크린샷 2020-04-06 오후 12 33 13](https://user-images.githubusercontent.com/62727831/78521273-49b4a800-7804-11ea-97ec-5443e1c14511.png)

![스크린샷 2020-04-06 오후 12 34 49](https://user-images.githubusercontent.com/62727831/78521280-4d482f00-7804-11ea-9525-85fe83bbc9bf.png)

* push


![스크린샷 2020-04-06 오후 12 35 16](https://user-images.githubusercontent.com/62727831/78521289-4faa8900-7804-11ea-8bc8-8207659556c7.png)

* 짜자잔


---

 ### Git 파일 관리 형태
  >
  > * 작업트리 - 인덱스 - 저장소
  >   * 인덱스에 파일 상태를 기록(stage-스테이징)
  >     저장소에 변경 사항을 기록하기 위해선 기록하고자 하는 모든 변경 사항들이 인덱스에 존재해야만 함
  >
  > - commited : 데이터가 local repository에 저장됨
  > - modified : 수정한 파일이 아직 로컬 저장소에 commit 되지 않음
  > - staged : 수정한 파일이 곧 commit 될 것을 표시 

---




 ### 브랜치
>
>  * 여러 개발자가 동시에 다양한 작업을 할 수 있게 만들어 주는 기능
>  * 메인 브랜치에서 자신의 작업 전용 브랜치에서 작업 후 메인 브랜치에서 병합,적용
>  * 저장소 처음 만들면 'master'라는 브랜치가 디폴트
>  * 통합 브랜치 : 언제든지 배포 가능한 버전 (모든 기능이 정상적 동작하는 상태, 즉 안정적 상태)
>  * 토픽 브랜치 : 기능 추가나 버그 수정과 같은 단위 작업을 위한 브랜치




>  * $ git brunch "이름"
>    * 브랜치 생성 
>    * 브랜치 제거 $ git brunch -d "이름"
>    * ex. git brunch "error_fix"
>
>  * $ git checkout "이름"
>    * 생성한 브랜치 사용하겠다고 명시 지정
>  * $ git checkout master
>    * 'master' 브랜치에 "HEAD"가 위치하게 전환
>  * $ git merge "커밋 이름"
>    * 메인 브랜치(master)에 통합

---



### 원격 저장소 -> 로컬 저장소로 불러오기(복제 = 다운로드)
>
>$ git clone 사용자명@호스트:/원격/저장소/경로

---



### 오류1 : fatal: remote origin already exists. (git remote add 사용시)
>
> * 원인 : 로컬 저장소가 이미 원격 저장소와 연결되어 있는데 또 다른 원격 저장소와 연결하려고 할 때 발생
> * 해결 : $ git remote rm origin 

---





### 오류2 : git push 충돌에러 (git push 사용시)
>
>! [rejected]    master -> master (fetch first)
>error: failed to push some refs to 'https://github.com/clineblue/TIL.git'
>
>* 원인 
>  * 로컬-원격 저장소의 상태가 달라서 발생. 
>  * git remote -v 로 상태 확인 후 git pull로 상태 동일하게 맞춰주기. 즉, 내 저장소가 최신 버전이 아닌 경우
>* 해결
>  * 병합(merge)작업. 다른 사람의 업데이트 이력을 내 저장소에도 갱신해야함
>  * $ git pull origin master
>    * 자동 병합
>  * $ vi README.md
>    * 편집기로 충돌된 부분 수정
>  * $ git add
>  * $ git commit -m "conflict_fix"
>  * $ git push -u origin master

![스크린샷 2020-04-05 오전 11 44 08](https://user-images.githubusercontent.com/62727831/78518748-4d443100-77fc-11ea-96ee-289504e43fca.png)


![스크린샷 2020-04-05 오전 11 43 44](https://user-images.githubusercontent.com/62727831/78518751-4e755e00-77fc-11ea-997c-de5a7815cba8.png)


### 오류3 : git pull 충돌에러 (git pull 사용시)

>error: Your local changes to the following files would be overwritten by merge:
>	README.md
>Please commit your changes or stash them before you merge.
>
>
>* 원인 
>
>   * 충돌되는 파일들이 존재. 
>   * remote repo에서 가져오려는 소스와 현재 local에 저장된 소스가 제대로 처리되지 않아 발생
>* 해결
>  * Git stash 활용.
>    * unstaged 파일들을 스택에 임시 저장하고 HEAD의 상태로 백업하는 것. 
>    * $ git stash // 임시 저장
>    * $ git pull // pull
>    * $ git stash pop // 임시 저장한 것 불러오기

---

