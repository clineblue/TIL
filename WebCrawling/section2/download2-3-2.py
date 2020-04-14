import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://api.ipify.org"

values = {
    'format' : 'json'
}
# 해당 사이트에서 원하는 형식
print('before', values)
params = urlencode(values)
#원하는 형태로 변환
print('after', params)



url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)