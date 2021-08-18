# Function1.py 
#리턴하지 않는 함수
def setValue(newValue):
    x = newValue
    print("함수내부:", x)

#호출
retValue = setValue(5)
print(retValue)

#다중의 값을 리턴하는 함수
def swap(x,y):
    return y,x 

#호출
print( swap(3,4) )

#디버깅 연습을 위한 교집합 함수
def intersect(prelist, postlist):
    #교집합 문자를 모아둘 지역변수(리스트)
    retList = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        #postlist에도 있고 retList에 아직 없으면 추가
        if x in postlist and x not in retList:
            retList.append(x)
    return retList 

#함수 호출
print( intersect("HAM","SPAM") )

#불변형식
print("---불변형식---")
a = 1.2 
print( id(a) )
a = 2.3
print( id(a) )

#가변형식
print("---가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#Pass By Reference 
wordlist = ["J","A","M"]
def change(x):
    #지역변수로 복사
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#함수 호출
change(wordlist)
print("함수 호출후:", wordlist)

#지역변수->전역변수->빌트인상수(LGB 이름해석규칙) 
#전역변수
x = 5 
def func1(a):
    return x+a

#호출
print( func1(1) )

def func2(a):
    #지역변수
    x = 1 
    return x+a 

#호출
print( func2(1) )
