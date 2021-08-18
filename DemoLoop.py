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


