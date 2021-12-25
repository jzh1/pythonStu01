# -*- coding:utf-8 -*-
# @Time : 2021/12/25 上午11:00
# @Author: jonas.jiang
# @File : fun4.py


def fun1(a, b, c):
    print('---------------- fun1------------------')
    print('a=', a)
    print('b=', b)
    print('c=', c)


def fun2(a, b, *, c, d):
    print('---------------- fun2------------------')
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# 参数调用时参数的传递，位置传参数
fun1(10, 20, 30)
# 列表中每一个元素转化为位置的实参传入
st = [11, 22, 33]
fun1(*st)
# 函数调用，所以是关键字实参
fun1(a=1, b=2, c=3)
# 函数调用，将字典中的关键字都转换为关键字实参传入
dic = {'a': 111, 'b': 112, 'c': 113}
fun1(**dic)

fun2(12, 22, c=1, d=2)
