# -*- coding:utf-8 -*-
# @Time : 2021/12/27 9:58 PM
# @Author: jonas.jiang
# @File : class3.py

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '已经' + str(self.age))


stu1 = Student('jzh', 23)
stu2 = Student('lb', 30)

print(id(stu1))
print(id(stu2))
print('--------------- 给stu2 添加属性，动态绑定性别属性   ----------------')
stu2.gender = '男'
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)

print('---------------  stu1 动态绑定方法show  ----------------')
stu1.eat()
stu2.eat()


def show():
    print('定义在类外的，所以称为函数，类内的为方法')


stu1.show = show
stu1.show()
