# -*- coding:utf-8 -*-
# @Time : 2021/12/18 下午11:07
# @Author: jonas.jiang
# @File : demoList1.py
# 列表切片(start stop step)
print('列表切片后ID不同')
lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print('old list：', id(lst))
lst2 = lst[1:6:1]
print('new cut list：', id(lst2))
print(lst[1:6:2])
print('负数索引：', lst[::-1])
