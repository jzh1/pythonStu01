# -*- coding:utf-8 -*-
# @Time : 2021/12/27 10:10 PM
# @Author: jonas.jiang
# @File : obj1.py

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('人的名字：' + self.name + ',人的年龄：' + str(self.age))


class Student(Person):
    def __init__(self, name, age, num):
        self.num = num
        super().__init__(name, age)

    def info(self):
        super().info()
        print('学生的的名字：' + self.name + ',学生的的年龄：' + str(self.age) + '学生的学号' + str(self.num))


class Teacher(Person):
    def __init__(self, name, age, year):
        self.year = year
        super().__init__(name, age)


print('---------------  重写student  ----------------')
stu = Student('jzh', 11, 961225)
teacher = Teacher('jzhTeach', 12, 35)

stu.info()
#teacher.info()
