# try1.py 

#함수를 정의
def divide(a,b):
    return a/b 

try:
    #호출
    result = divide(5,2)
except TypeError:
    print("숫자 형식이어야 합니다.")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
else:
    print("결과:{0}".format(result))
finally:
    print("한번 더 체크(이중체크)")


print("전체 코드 실행 종료")

