# -*- coding:utf-8 -*-
# @Time : 2021/12/20 8:37 PM
# @Author: jonas.jiang
# @File : view.py
print('--------------- get key and get value   ----------------')
score = {'jzh': 199, 'lili': 123, 'xiaoming': 12}
keys = score.keys()
values = score.values()
print(keys, type(keys))
print(values, type(values))
print(list(keys))
print(list(values))
print('--------------- key value   ----------------')
# 元组
items1 = score.items()
print(items1, type(items1), list(items1))
