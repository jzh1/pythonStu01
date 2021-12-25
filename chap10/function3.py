# -*- coding:utf-8 -*-
# @Time : 2021/12/25 上午10:46
# @Author: jonas.jiang
# @File : function3.py


def fun3(*aged):
    print('------------------ 个数可变的位置参数,一个方法只能定义一个，结果为元祖 ----------------')
    print(aged)


def fun4(**aged):
    print('------------------ 个数可变的关键字型参，一个方法只能定义一个，结果为字典 ----------------')
    print(aged)


# 可以的
def fun5(*a, **b):
    print('------------------ 合并使用 ----------------')
    print(a)
    print(b)


# 不可以的
''' def fun6(**a,*b):
    pass '''

fun3(1)
fun3(1, 2)
fun3(1, 2, 3)
fun4(a=1, b=2, c=3)
fun5(1, 2, a=1, b=2, c=3)
