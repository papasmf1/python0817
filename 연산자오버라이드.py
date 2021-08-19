#연산자 오버라이드(의미를 변경) 
class NumBox:
	def __init__(self, num):
		self.Num = num
	# +연산자의 메서드명
	#일반 인스턴스 메서드 
	def add(self, num):
		self.Num += num
	# -연산자의 메서드명
	def remove(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n.add(100)
print(n.Num)
n.remove(50)
print(n.Num)
