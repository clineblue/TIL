from urllib.parse import urljoin

baseurl = "http://test.com/html/a.html" # 가정
print(">>", urljoin(baseurl, "b.html"))
# 치환  http://test.com/html/b.html
print(">>", urljoin(baseurl, "sub/b.html"))
# 절대 경로는 묶어놓고, 나머지 아래 파일은 내가 변경할 수 있음
# http://test.com/html/sub/b.html
print(">>", urljoin(baseurl, "../index.html"))
# 한 번 상대경로 위로 올라갔으니 .com/ 이하
# http://test.com/index.html
print(">>", urljoin(baseurl, "../img/img.png"))
# http://test.com/img/img.png

#url을 합쳐주는거.
