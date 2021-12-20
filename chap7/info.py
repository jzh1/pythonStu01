# -*- coding:utf-8 -*-
# @Time : 2021/12/20 8:49 PM
# @Author: jonas.jiang
# @File : collect.py
print('---------------    ----------------')
items = ['jzh1', 'jzh3', 'jzh2']
price = [11, 22, '33q',22]
lst = zip(items, price)
print(list(lst))

lst2 = {items: price for items, price in zip(items, price)}
print(lst2)

lst3 = {items.upper(): price for items, price in zip(items, price)}
print(lst3)
