# -*- coding:utf-8 -*-
# @Time : 2021/12/22 10:46 PM
# @Author: jonas.jiang
# @File : function.py

# a b 形式参数
def calc(a, b):
    c = a + b
    return c


# 位置传参数 实际参数
sums = calc(1, 2)
print(sums)

# 关键字传参（关键字写错，就会变为位置传递参数）
a = 10
b = 20
sums = calc(b, a)
print(sums)

# 位置传参
a = 10
c = 20
sums = calc(c, a)
print(sums)
