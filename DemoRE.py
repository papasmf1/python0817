# DemoRE.py 
import re 

#매칭함수(매칭객체라 리턴됨) 
result = re.match("[0-9]*th", "35th")
print( result )
print( result.group() )

#서치함수 
result = re.search("[0-9]*th", "35th")
print( result )
print( result.group() )

print("---함정이 있는 경우---")
result = re.match("[0-9]*th", "  35th")
# print( result )
# print( result.group() )

#서치함수 
result = re.search("[0-9]*th", "  35th")
print( result )
print( result.group() )

#단어나 우편번호 검색 
print( bool(re.match("apple", "this is apple")) )
print( bool(re.search("apple", "this is apple")) )
print("---우편번호---")
print( bool(re.search("\d{5}", "우리동네는 52300")) )
print( bool(re.search("\d{4}", "올해는 2021년")) )


