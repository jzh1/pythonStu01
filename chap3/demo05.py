# -*- coding:utf-8 -*-
# @Time : 2021/12/16 下午11:44
# @Author: jonas.jiang
# @File : demo05.py

# 链式赋值
a = b = c = 30
print(a, id(a))
print(b, id(b))
print(c, id(c))
# 参数赋值

# 解包赋值
a, b = 10, 11
print('交换前', a, b)
a, b = b, a
print('交换后', a, b)
