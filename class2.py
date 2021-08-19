# class2.py 
#클래스를 정의
class Person:
    #주로 데이터를 공유할 때의 클래스 멤버 변수의 위치
    num_person = 0 
    #인스턴스의 멤버 변수 초기화를 담당하는 특별한 메서드(생성자)
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1 
    #인스턴스 메서드 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person() 
p3 = Person() 
print("인스턴스 갯수:", Person.num_person)

#인스턴스에 추가
p1.age = 30
print( p1.age )
#print( p2.age )

