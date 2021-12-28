# -*- coding:utf-8 -*-
# @Time : 2021/12/27 10:10 PM
# @Author: jonas.jiang
# @File : obj1.py

class Person(object):
    def __init__(self, name, age):
        print('默认继承object，不写也没关系')
        self.name = name
        self.age = age

    def info(self):
        print('人的名字：' + self.name + ',人的年龄：' + str(self.age))


class Student(Person):
    def __init__(self, name, age, num):
        self.num = num
        super().__init__(name, age)


class Teacher(Person):
    def __init__(self, name, age, year):
        self.year = year
        super().__init__(name, age)


class A:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class B:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class C(A, B):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        # super().__init__(name)


print('---------------  单继承使用  ----------------')
stu = Student('jzh', 11, 961225)
teacher = Teacher('jzhTeach', 12, 35)

stu.info()
teacher.info()

print('---------------  多继承使用  ----------------')
c = C('jzh')
c.show()
