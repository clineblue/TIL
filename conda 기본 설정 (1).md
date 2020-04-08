### 아나콘다 가상환경 

* $ conda info --envs 
  * 가상환경 확인

### 가상환경 생성시 오류 (채널 오류)

1. 배경
   * 가상환경을 새로 생성
   * $ conda create --name "가상환경 명" "설치할 환경"
   * packagesNotFoundError 발생

2. 원인
   * conda가 패키지를 검색할 때 채널을 찾지 못하는 상황

3. 해결

   * conda에서 표준 채널을 통해 패키지를 사용할 수 있도록 표준 패키지 설정

   * $ conda config --append channels conda-forge

### pip로 패키지 설치시 오류

1. 배경
   * $ pip install simplejson 명령어를 통해 json을 설치하려함
   * RuntimeError : Python 3.5 or later is required
2. 원인
   * Python 버전이 낮아 설치가 불가능
   * current version :  3.4.5
3. 해결
   * conda UI를 통해 임의 업그레이드 진행 

### 가상환경 삭제 오류

1. 배경

   * 이전에 설치한 여러 가상환경을 제거하려고 함
   * conda remove --name "가상환경 명" --all
   * No such file or directory 에러

2. 원인 ( 내가 생각한)

   * 스택플로우에서는 1. 표준 활성화 파일이 없다 2. 일부 패키지가 손상되었을 것이다. 3. 가상환경 설치시 환경 변수 경로를 설정해주어야 한다.
   * bash_profile 파일에 접속하여 conda 환경 변수 경로 확인했으나 이상이 없는 듯 보이고 다른 문제를 확인

3. 해결

   * 임시방편으로 해결된 듯한 느낌이 있지만 그래도 되었으니.
   * $ conda deactivate 
     * 비활성화시 다시 (base) 로 가상환경이 리턴

   * $ conda remove --name "환경 명" --all
     * 비활성화 후 다시 입력시 삭제되어짐.



### TIL

1. 맥 터미널 색상변경
   * $ sudo vi ~/.bash_profile
   * 터미널을 커스터마이징 해보았다.

2. 환경변수란
   * 셸은 여러 가지 환경 변수 값을 가짐
   * 설정된 환경 변수는 'echo $ 환경 변수이름' 형식으로 명령어 실행
   * ex) 'echo $HOSTNAME'

3. kim@blue-MacBook-Air: 
   * 사용자 이름 : kim
   * 호스트 이름 : blue
