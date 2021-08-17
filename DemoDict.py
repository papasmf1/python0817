# DemoDict.py 
d = dict(a=1, b=2, c=3)
print( d )
print( type(d) )

#딕셔너리는 아래와 같이 초기화 
color = {"apple":"red", "banana":"yellow"}
print( color )
print( len(color) )
#검색
print( color["apple"] )
#입력
color["cherry"] = "red"
print( color )
#삭제
del color["apple"]
print( color )
#반복 구문
for item in color.items():
    print(item)

for k,v in color.items():
    print(k, v)

#전화번호를 딕셔너리(사전구조)에 저장
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print( phone["park"] )
print( "park" in phone )
print( "moon" not in phone )

#참조를 복사
p = phone 
phone["kang"] = "1234"
print( phone )
print( p )
print( id(phone) )
print( id(p) )

for key in phone.keys():
    print(key)

for value in phone.values():
    print(value)







