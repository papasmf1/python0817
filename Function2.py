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


#기본값이 셋팅된 함수(PlanA, PlanB, PlanC....) 피보팅~~ 
def times(a=10, b=20):
    return a*b 

#호출 
print( times() )
print( times(5) )
print( times(b=6) )
print( times(5,6) )

#키워드 인자 방식(매개변수명을 기술)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="8080", server="test.com") )

#가변인자(갯수가 정해지지 않은 경우): *는 Tuple형태로 받겠다. 
def union(*ar):
    #지역변수 초기화
    result = []
    # HAM(0) | EGG(1)
    for item in ar:
        # H(0) | A(1) | M(2)
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )
