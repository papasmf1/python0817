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