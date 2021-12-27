# -*- coding:utf-8 -*-
# @Time : 2021/12/27 11:07 PM
# @Author: jonas.jiang
# @File : obj6.py

a = 100
b = 10
print('---------------  加法运算本质上是进行 __add__ 操作，下面的class之间的加减可以证明   ----------------')
c = a + b
d = a.__add__(b)
print(c)
print(d)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.name + other.name


stu1 = Student('jzh', 11)
stu2 = Student('lb', 20)
stu3 = stu1 + stu2
print(stu1.__add__(stu2))
print(stu3)

print('---------------  __len__()  ----------------')
lst = [1, 2, 3, 4]
print(len(lst))
print(lst.__len__())
