
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 클래스 변수, 인스턴스 변수

class Warehouse:
    stock_num = 0 #클래스 변수
    def __init__(self,name): # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('kim')
user2 = Warehouse('lee')
print(user1.name)
print(user2.name)
print(user1.__dict__) #stock_num은 나오지 않음, 본인 인스턴스엔 없으니까
print(user2.__dict__) # user의 네임스페이스 확인
print(Warehouse.__dict__) #stock num = 2 , 위 user1, user2 에서 2번 실행이 되었으니까

print(user1.stock_num) # 인스턴스 네임스페이스에서 찾고 없으면 > 클래스 네임스페이스에서 찾아서 출력. =2
print(user2.stock_num) # 클래스 변수(공유)