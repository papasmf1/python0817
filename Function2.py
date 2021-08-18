# Function2.py
#전역변수
g = 1 
#함수 정의
def testScope(a):
    #불변형식을 내부에 참조를 땡겨와서 읽기 + 쓰기 
    #global g 
    g = 2 
    return g+a 

#호출
print( testScope(1) )
print("전역변수 g:", g)

