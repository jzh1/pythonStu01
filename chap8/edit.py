# -*- coding:utf-8 -*-
# @Time : 2021/12/20 9:10 PM
# @Author: jonas.jiang
# @File : edit.py
# 元组内引用不变
# 元组内对象本事是可变的，那么可编辑
# 元组内对象本身是不可变得，那么不可编辑
ls = (11, [12, 34], 44)
print(ls, type(ls))
print(ls[0], type(ls[0]), id(ls[0]))
print(ls[1], type(ls[1]), id(ls[1]))
print(ls[2], type(ls[2]), id(ls[2]))
print('--------------- change ls[1]   ----------------')
ls[1].append(33)
print(ls)
