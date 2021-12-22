# -*- coding:utf-8 -*-
# @Time : 2021/12/22 10:59 PM
# @Author: jonas.jiang
# @File : funMoney.py
def fun(arg1, arg2):
    print('arg1', arg1)
    print('arg2', arg2)
    arg1 = 100
    arg2.append(111)
    print('arg1', arg1)
    print('arg2', arg2)


n1 = 11
n2 = [11, 22, 33]
print('--------------- fun before    ----------------')
print('n1=>', n1)
print('n2=>', n2)
print('--------------- fun after    ----------------')
fun(n1, n2)
print('n1=>', n1)
print('n2=>', n2)

print('---------------  n1 不可变对象在函数传递过程中不可变   ----------------')
print('---------------  n2 可变对象在函数传递过程中可变   ----------------')