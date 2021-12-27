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


print('---------------  Student(类对象) 的分析  ----------------')
print(Student, id(Student), type(Student))
print()
print('---------------  Student(实例对象-根据类对象创建的) 的分析  ----------------')
stu = Student('jzh', 25)
print(id(stu), type(stu), stu)
print()
# 输出：4527945520 <class '__main__.Student'> <__main__.Student object at 0x10de2f730>
# 分析：4527945520 的十六进制等于 0x10de2f730

print('---------------  Student(实例对象) 的使用(使用点"."调用:对象.方法名)  ----------------')
stu.eats()
stu.method()
print(stu.name)
print(stu.age)

print('---------------  Student(实例对象) 的使用(使用点"."调用：类.方法名(self) self实际上是本身的对象)  ----------------')
Student.eats(stu)


