# -*- coding:utf-8 -*-
# @Time : 2021/12/27 11:07 PM
# @Author: jonas.jiang
# @File : obj6.py
print('--------------- __new__创建对象在前，__init__初始化对象在后   ----------------')
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__ 被调用执行 cls的id,{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建对象的id,{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__ 被调用执行 self 的id,{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object 对象的ID，{0}'.format(id(object)))
print('person对象的ID，{0}'.format(id(Person)))
p1 = Person('jzh', 23)
print('p1对象的ID，{0}'.format(id(p1)))
