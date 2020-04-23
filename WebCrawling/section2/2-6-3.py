import sys
import io
from bs4 import BeautifulSoup


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("cars.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func =", soup.select_one(selector).string)

car_lambda = lambda q : print("car_lambda", soup.select_one(q).string)

car_func('#gr')
#왜 '' 안쓰면 에러가 생기는 거지 이해가 안가네
car_func('li#gr')
car_func("ul > li#gr")
car_func("li[id='gr']")


car_lambda('#gr')
car_lambda('li#gr')
car_lambda("ul > li#gr")
car_lambda("li[id='gr']")
print(soup.select("li")[3].string)

#람다식
