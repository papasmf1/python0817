# DemoLoop2.py 

#리스트 컴프리헨션(리스트 내장)
lst = list(range(1,11))
result = [i**2 for i in lst if i > 5]
print( result )

tp = ("apple", "orange", "kiwi")
print( [len(i) for i in tp] )
#사전구조(dict)
d = {100:"apple", 200:"orange", 300:"kiwi"}
print( [v.upper() for v in d.values()] )

