# DemoLoop.py

d = {"apple":100, "orange":200, "kiwi":300}

for k,v in d.items():
    print(k, v )

#구구단 출력
#중단점, 중지점(Break Point)
#디버깅하는 모드면 무조건 중지 
for x in [2,3,4,5,6]:
    print("---{0}단---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))


#탈출구문 
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    #선택한 블럭을 주석 처리: ctrl + / 
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("---continue구문---")
for i in lst:
    #선택한 블럭을 주석 처리: ctrl + / 
    if i % 2 == 1:
        continue
    print("Item:{0}".format(i))

#수열함수 
print( range(10) )
result = list(range(10))
print( result )
print( list(range(1,11)) )
print( list(range(10,0,-1)) )
print( list(range(2000, 2022)) )

#for루프를 수동으로 조절
for i in range(10):
    print(i)


print("전체 코드 실행 종료")



