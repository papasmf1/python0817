# class1.py 
#클래스를 정의
class Person:
    #인스턴스의 멤버 변수 초기화를 담당하는 특별한 메서드(생성자)
    def __init__(self):
        self.name = "default name"
    #인스턴스 메서드 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person() 
p1.name = "전우치"
#런타임(실행시간)시에 변수를 추가<--->디자인타임(코딩중)
Person.title = "new title"

print( p1.title )
print( p2.title )
print( Person.title )



    

