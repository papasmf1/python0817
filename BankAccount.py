# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    #생성자 메서드 
    def __init__(self, id, name, balance):
        #인스턴스의 멤버 변수 초기화 
        #내부에 멤버 숨김(__)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금
    def deposit(self, amount):
        self.__balance += amount 
    #출금
    def withdraw(self, amount):
        self.__balance -= amount
    #문자열 리턴(object에 정의된 약속된 메서드) 
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account2 = BankAccount(200, "이순신", 20000)
account1.deposit(5000)
account1.withdraw(3000)
#외부에서 접근 
#print(account1.__balance) 
#이름 변경(백도어)
print(account1._BankAccount__balance) 
print(account1)

#인스턴스에 추가
account1.balance = 1500 
print(account1.balance)
#print(account2.balance)

print( account1.__dict__ ) 
print( account2.__dict__ ) 
print( BankAccount.__dict__ ) 
print( dir() )


