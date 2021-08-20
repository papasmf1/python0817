# DemoStr.py 

#print( dir(str) )
#메뉴얼에서 str찾기 

#반복적인 문구 생성
names = ["홍길동","이순신","전우치"]
for name in names:
    print("안녕하세요 더운 여름입니다. {0}님".format(name))
    print("=" * 40)

#str형식의 메서드들 사용 
print( "demo.ppt".endswith("ppt") )
print( "python is powerful".capitalize() )
print( "python is powerful".count("p") )
print( "python is powerful".count("p", 7) )


