import sys
number1 = 123
number2 = 456
print("123 + 456 =",number1+number2)
list1 = [1,'2',3,'4']
print(list1)
list2 = [x*2 for x in range(100) if x%2==0]
print(list2)
# for i in range(len(list2)):
#     print(list2[i])
string1 = "123456"
tuple1 = (1,2,3,4,5,6)
#x[a:b], from a to b-1
print(tuple1[0:3])  #1,2,3
print(tuple1[-2:6])  #5,6
print(tuple1[-5:-2]) #2,3,4
tuple2 = tuple1 * 2
print(tuple2)
tuple2 = (7,8,9)
print(tuple1+tuple2)
print(5 in tuple1)
print(9 in tuple1)
name = ['a','b','c']
value = [1,2,3]
dict1 = dict(zip(name, value))
dict1['d'] = 4
dict1.pop('a')
print(dict1)
set1 = {1,2,3,4,5,6}
set2 = {1,3,5,7}
print(set1-set2)
print(set1|set2)
print(set1&set2)
print(set1^set2)