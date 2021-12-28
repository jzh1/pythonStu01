# -*- coding:utf-8 -*-
# @Time : 2021/12/29 12:27 AM
# @Author: jonas.jiang
# @File : demo1.py
import os
print('---------------  read  ----------------')
file = open('../test.txt', 'r')
print(file.readlines())
file.close()

