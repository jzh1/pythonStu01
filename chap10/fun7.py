# -*- coding:utf-8 -*-
# @Time : 2021/12/25 上午11:31
# @Author: jonas.jiang
# @File : fun7.py


def fun1(n):
    if n == 1 or n == 2:
        return n
    else:
        return fun1(n - 1) + fun1(n - 2)


print(fun1(6))