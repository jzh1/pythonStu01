# -*- coding:utf-8 -*-
# @Time : 2021/12/20 9:16 PM
# @Author: jonas.jiang
# @File : collect.py
print('---------------  create  ----------------')
co = {1, 2, 4, 44, 44}
print(co, type(co))

co2 = set(range(1, 5))
print(co2, type(co2))

# 去重，无序
co3 = set([13, 12313, 33434, 11, 11, 22, 22])
print(co3, type(co3))

co4 = set({12, 3, 4, 5, 6})
print(co4, type(co4))

co5 = set()
print(co5, type(co5))
