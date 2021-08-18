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

