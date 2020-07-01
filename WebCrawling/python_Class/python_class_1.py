
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("----------")
        print("name: " +self.name)
        print("phone: " +self.phone)
        #메소드

user1 = UserInfo()
user2 = UserInfo()
# 인스턴스화 : class로 부터 객체를 만드는 과정

#print(id(user1)) #4329736400 ref ID가 나

user1.set_info("kim", "010-5555-7777")
user2.set_info("lee", "010-3333-5555")
# 인스턴스된 객체가 클래스의 메서드 사용

user1.print_info()
user2.print_info()
# 객체가 클래스의 메서드 사

print(user1.__dict__) #네임스페이스를 볼 수 있음, 딕셔너리 형태
print(user2.__dict__)

print(user1.phone,user1.name)