
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print("function1 called!")
    def function2(self):
        print(id(self))
        print("function2 called!")

f = SelfTest() #인스턴스
#print(dir(f))
#f.function1() # Error : TypeError: function1() takes 0 positional arguments but 1 was given
print(id(f))
f.function2()
# 호출됨 # 자동으로 무언가 넘어간다. 즉, self가 넘어간다
#4468348800
#4468348800 f인스턴스와 self의 주소값이 일치. = 자동으로 인스턴스 주소값이 self에 담겨 전달이 된다.
print(SelfTest.function1()) #인스턴스화 시키지 않고, 직접적으로 호출하면 호출이 됨

#