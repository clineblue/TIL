
import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#json array : {'key' : 'value'} 딕셔너리형태(키,밸류값)로 표시!
#json형태를 어레이 형태로 준다면 json으로 바로 키,밸류값을 알 수 있었고
with requests.Session() as s:
    #r = s.get('http://httpbin.org/get')
    #print(r.status_code) # 응답코드
    #print(r.ok) # 서버가 확실히 오픈상태인지 확인
    r = s.get('https://jsonplaceholder.typicode.com/post/1')
    print(r.text)
    print(r.json()) #가공을 해서 값을 줌
    print(r.json().keys())
    print(r.json().keys())
    print(r.encoding)
    print(r.content)
    print(r.raw)
