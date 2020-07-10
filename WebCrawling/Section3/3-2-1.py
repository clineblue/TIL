
import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session() #세션 연결
#r = s.get('https://www.naver.com') #request
#print('1', r.text)

#r = s.get('http://httpbin.org/cookies',cookies={'from':'myname'})
#print(r.text)

url = 'http://httpbin.org/get'
headers = {'user-agent' : 'myApp_1.0'}
r = s.get(url,headers=headers)
print(r.text)

s.close() #리소스 낭비 방지.

with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)