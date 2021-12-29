# -*- coding:utf-8 -*-
# @Time : 2021/12/29 9:04 PM
# @Author: jonas.jiang
# @File : demo5.py

import os

path = os.getcwd()
lst = os.listdir(path)

for filename in lst:
    if filename.endswith('.py'):
        print(filename)

