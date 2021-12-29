# -*- coding:utf-8 -*-
# @Time : 2021/12/29 9:19 PM
# @Author: jonas.jiang
# @File : demo6.py
import os

path = os.getcwd()
lst_file = os.walk(path)

for dirpath, dirname, filename in lst_file:
    print(dirpath, dirname, filename)
    print('---------------    ----------------')
