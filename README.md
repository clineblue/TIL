## 20.04.03

#### Git 초기 설정하기

##### 1. 터미널로 설정하기

1.  repository 만들기

* remote repository 만들기 
  // git-hub홈페이지에서 만들기

* local repository 만들기 
  // 코딩할 폴더 만들기 

  * mkdir GitStart
  * cd Gitstart
  * git config --global user.name "이름" 
    // git commit에 사용될 username
  * git config --global user.email "가입한 email" 
    // git commit에 사용될 e-mail
  * echo "GitStart" >> README.md
    //  echo 명령어는 새로운 파일(READMD라는 마크애니 문법파일), 그 파일의 내용을 생성(GitStart)
  * git init
    // 로컬 저장소를 초기화 하는 명령어 즉, "여기가 로컬 저장소야"라고 알려주는 명령어
  * git status 
    // local repository 상태 확인
  * git add README.md 
    // 해당 파일 staged 상태로 만들기 or 깃 목록에 파일 추가
    // git add . > 디렉토리 내 모든 파일 올리기

  > Git 파일 관리 형태
  >
  > - commited : 데이터가 local repository에 저장됨
  > - modified : 수정한 파일이 아직 로컬 저장소에 commit 되지 않음
  > - staged : 수정한 파일이 곧 commit 될 것을 표시 

  

  * git commit -m "코멘트"
    // staged -> commited상태로 변환
    // local에 저장(커밋)
  * git remote add origin https://주소
    // local과 remote repository 연결 설정
  * git push -u origin master
    // local -> remote repository로 전송
    // remote repository에 master라는 branch를 생성

