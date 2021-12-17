# 比较运算符
a, b = 10, 33
print('a<b ?', a < b)
print('a>b ?', a > b)
print('a==b ?', a == b)
print('a=<b ?', a <= b)
print('a>=b ?', a >= b)
print('a!=b ?', a != b)

# is， is not 比较的是ID
a = 10
b = 10
print(a == b)
print(a is b)

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(list1 is list2)
print(id(list2), id(list1))
