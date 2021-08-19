#부모 클래스 정의 
class Person:
    def __init__(self, name, phoneNumber):
        #인스턴스 멤버 변수
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스 정의
class Student(Person):
    #덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #자기자신을 가리키는 self, this 
        #부모를 가리키는 base, super키워드가 없다~~ 
        #명시적으로 부모의 생성자 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기(커스터마이징, 재정의)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(
            self.subject, self.studentID))


#인스턴스 생성 
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
# print( p.__dict__ )
# print( s.__dict__ )
p.printInfo()
s.printInfo()


