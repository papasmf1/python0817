# 메모리관리.py 

class MyClass:
    #생성자 메서드(초기화 담당)
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    #소멸자 메서드(유명무실)
    def __del__(self):
        print("Instance is deleted!")

d = MyClass(5)
#참조 카운트(1->0) 스스로 소멸 
#del d 

print("전체 코드 실행 종료")
