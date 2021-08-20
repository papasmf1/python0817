# DemoFile.py 

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3) )

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3) )

#서식을 문자로 지정
print("{0:x}".format(10) )
print("{0:b}".format(10) )
#화폐를 출력
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

#파일을 생성해서 쓰기
f = open("c:\\work\\demo.txt", "wt")
f.write("한글\nabcd\n1234\n")
f.close()

#파일을 읽기 
f = open("c:\\work\\demo.txt", "rt")
print( f.read() )

f.close() 


