# -*- coding:utf-8 -*-
# @Time : 2021/12/27 11:07 PM
# @Author: jonas.jiang
# @File : obj6.py

class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name):
        self.name = name


x = C('jzh')
print('---------------  实例对象的属性字典   ----------------')
print(x.__dict__)
print('---------------  类对象的属性字典   ----------------')
print(C.__dict__)
print('---------------  对象所属   ----------------')
print(x.__class__)
print('---------------  父类类型元素   ----------------')
print(C.__bases__)
print('---------------  类的基类   ----------------')
print(C.__base__)
print('---------------  类的层次结构   ----------------')
print(C.__mro__)
print('---------------  子类列表   ----------------')
print(A.__subclasses__())