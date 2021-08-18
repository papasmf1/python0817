# DemoLogic.py 
#불린형식(bool)
isRight = True 
print( type(isRight) )
print( 1 < 2 )
print( 1 != 2 )
print( 1 == 2 )

#and(~이면서) or(~이거나)
print( True and True and True )
print( True and True and False )
print( True or False or False )

print("---파이썬 판단 근거----")
print( bool(0) )
print( bool(-1) )
print( bool(1) )
print( bool("") )
print( bool("demo") )
print( bool(None) )
print( bool([]) )
print( bool([1,2,3]) )


#얕은 복사(참조만 전달)
a = [1,2,3]
b = a 
a[0] = 38
print( a )
print( b )
print( id(a) )
print( id(b) )

#깊은 복사는 원본과 복사본을 따로 만들기
a = [10,20,30]
b = a[:]
a[0] = 11 
print( a )
print( b )
print(id(a))
print(id(b))

#리스트가 아닌 경우는 copy모듈 사용
import copy 
a = [100, 200, 300]
b = copy.deepcopy(a)
a[0] = 101 
print( a )
print( b )
print(id(a))
print(id(b))

