# -*- coding:utf-8 -*-
# @Time : 2021/12/29 12:27 AM
# @Author: jonas.jiang
# @File : demo1.py
import os
print('---------------  w  ----------------')
file = open('../test1.txt', 'w')
file.write('python')
file.close()

print('---------------  copy  ----------------')
rb = open('../test.txt','rb')
wb = open('../cppytest.txt','wb')

wb.write(rb.read())
wb.close()
rb.close()