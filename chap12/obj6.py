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


c = C('jzh')
print(c.__dict__)
