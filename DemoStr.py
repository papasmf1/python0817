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

#숫자인지, 문자열인지? 
print( "MBC2580".isalnum() )
print( "MBC:2580".isalnum() )
print( "2580".isdecimal() )

#문자열의 길이
print( len("한글") )

print("---앞뒤의 공백문자 제거---")
u = "<<<  spam and ham  >>>"
print(u)
result = u.strip("<> ")
print(result)
#치환
result = result.replace("spam", "spam egg")
print(result)
#리스트로 받기
lst = result.split() 
print( lst )
print("---문자열로 합치기---")
print( ":)".join(lst) )


