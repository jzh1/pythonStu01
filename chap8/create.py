# -*- coding:utf-8 -*-
# @Time : 2021/12/20 8:58 PM
# @Author: jonas.jiang
# @File : create.py
print('---------------  three create  ----------------')
ls = (11, 22, 34, 55)
ls2 = tuple((11, 22, 'eeee'))
ls3 = 11, 22, 33, 44, 55
# = ls4 = (12,)
ls4 = 12,
print(ls, type(ls))
print(ls2, type(ls2))
print(ls3, type(ls3))
print(ls4, type(ls4))

print('--------------- list dict tuple   ----------------')
lst1 = []
lst2 = list()

lst3 = {}
lst4 = dict()

lst5 = ()
lst6 = tuple()
print(lst1, type(lst1))
print(lst2, type(lst2))
print(lst3, type(lst3))
print(lst4, type(lst4))
print(lst5, type(lst5))
print(lst6, type(lst6))
