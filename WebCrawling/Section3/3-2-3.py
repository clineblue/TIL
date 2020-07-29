#stream 데이터를 json으로 변환해서 그 안에 있는 키 값에 대한 정보를 출력하는 코드
import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


with requests.Session() as s:
    r = s.get('http://httpbin.org/stream/20')
    #print(r.text) # 키와 벨류로 이루어진 json데이터 인 것 같음
    #print(r.encoding) # = None
    #print(r.json()) # 에러 / 즉, 직렬, 스트림형태로 쭉 이어진 자료더라.
    if r.encoding is None:
        r.encoding = 'utf-8'

    for line in r.iter_lines(decode_unicode=True): #기본값
        #print(line)

        b = json.loads(line)
        print(b['origin']) #origin이라는 키. #Re: 39.112.248.140
        print(type(b)) # <class 'dict'>
        for e in b.keys():
            print('key =',e, 'values =', b[e]) #각각의 키와 벨류값이 나옴

