
import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#세션 연결
s = requests.Session()
#요청(request)
#r = s.get('https://www.naver.com')
#print(r.text)

#r = s.get('http://httpbin.org/cookies',cookies={'from':'myname'})
#print(r.text)

url = 'http://httpbin.org/get'
headers = {'user-agent' : 'myApp_1.0'}
r = s.get(url,headers=headers)
print(r.text) # 반응값으로 host: httpbin.org / User-Agent : myapp_1.0이 리턴

s.close() #리소스 낭비 방지.
#with 구문으로도 표시가능
#with requests.Session() as s:
#    r = s.get('https://www.naver.com')
#    print(r.text)
