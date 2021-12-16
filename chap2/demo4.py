# -*- coding:utf-8 -*-
# @Time : 2021/12/16 下午11:02
# @Author: jonas.jiang
# @File : demo4.py

# ------- 浮点类型----------
n1 = 1.1
n2 = 2.2
print(n1 + n2)

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))
