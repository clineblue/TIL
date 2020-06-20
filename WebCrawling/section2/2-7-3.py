from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/courses/it-programming/web-dev"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")
WebRecommend = soup.select("div.card-content")
#print(WebRecommend)
#정상 출력
for i,e in enumerate(WebRecommend, 1):
    print(i,e.select_one("div.course_title").string)

