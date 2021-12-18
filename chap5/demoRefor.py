# -*- coding:utf-8 -*-
# @Time : 2021/12/18 下午1:07
# @Author: jonas.jiang
# @File : demoRefor.py
# 嵌套循环
print('-------------- 矩形--------------')
for i in range(1, 5):
    for j in range(0, 5):
        print('*', end='\t')
    print()

print('-------------- 三角形--------------')
for i in range(1, 10):
    for j in range(0, i):
        print('*', end='\t')
    print()

print('-------------- 99乘法表--------------')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end='\t')
    print()
