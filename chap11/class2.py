# -*- coding:utf-8 -*-
# @Time : 2021/12/27 9:16 PM
# @Author: jonas.jiang
# @File : class1.py


class Student:
    # 类属性
    native = '吉林'
    name = 'init_jzh'

    # 实例方法
    def eats(self):
        print(' 实例方法eat!!!!,学生在吃饭')

    # 静态方法
    @staticmethod
    def method():
        print('staticmethod 静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('类方法 classmethod')

    def __init__(self, name, age):
        print('初始化方法')
        # 实例属性，赋值操作
        self.name = name
        self.age = age


def pa():
    print('---------------  在类之外定义的为函数，在类内定义的叫做方法  ----------------')


# 类属性的使用方式
print(Student.native)
stu1 = Student('zhangsan', 23)
stu2 = Student('lisi', 30)
print(stu1.native)
print(stu2.native)
print('--------------- 修改类属性   ----------------')
Student.native = '山东'
print(Student.native)
print(stu1.native)
print(stu2.native)

print('--------------- 修改类对象属性   ----------------')
stu1.native = '上海'
stu2.native = '北京'
print(Student.native)
print(stu1.native)
print(stu2.native)

print('--------------- 类方法   ----------------')
Student.cm()
