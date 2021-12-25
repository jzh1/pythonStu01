# -*- coding:utf-8 -*-
# @Time : 2021/12/25 上午11:16
# @Author: jonas.jiang
# @File : fun5.py


# 局部变量
def fun1(a, b):
    print(a)
    print(b)


# 全局变量
name = "jzh"


def fun2():
    print(name)


fun2()


def fun3():
    # 函数内声明全局变量
    global age
    age = 110


fun3()
print(age)
