# -*- coding:utf-8 -*-
# @Time : 2021/12/25 上午11:23
# @Author: jonas.jiang
# @File : fun6.py


def fun1(n):
    if n == 1:
        return 1
    else:
        return n * fun1(n - 1)


def fun2(n):
    t = 1
    for i in range(1, n+1):
        t *= i
    return t


x = fun1(6)
print(x)
x1 = fun2(6)
print(x1)