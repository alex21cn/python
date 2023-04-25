import sys
a = 123
b = 456
print("123 + 456 =",a+b)
myList = [x*2 for x in range(100) if x%2==0]
print(myList)
# for i in range(len(myList)):
#     print(myList[i])
x = "123456"
x = (1,2,3,4,5,6)
#x[a:b], from a to b-1
print(x[0:3])  #1,2,3
print(x[-2:6])  #5,6
print(x[-5:-2]) #2,3,4
y = x * 2
print(y)
y = (7,8,9)
print(x+y)
print(5 in x)
print(9 in x)
name = ['a','b','c']
value = [1,2,3]
myDict = dict(zip(name, value))
myDict['d'] = 4
myDict.pop('a')
print(myDict)