#전역변수 
str = "Not Class Member"
# 파이썬은 모호한 것 보다는 명확한 것이 좋다~~ 
class GString:
    def __init__(self):
        #인스턴스 멤버 변수 
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 실수
        print(self.str)

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
