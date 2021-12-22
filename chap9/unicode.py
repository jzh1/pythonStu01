# -*- coding:utf-8 -*-
# @Time : 2021/12/22 10:37 PM
# @Author: jonas.jiang
# @File : unicode.py
s = '天涯共此时'
print('---------------  转码  ----------------')
# 一个中文占两个
print(s.encode(encoding='GBK'))
# 一个中文占三个
print(s.encode(encoding='UTF-8'))

print('---------------  解码  ----------------')
byte = s.encode(encoding='GBK')
byte2 = s.encode(encoding='UTF-8')
print(byte.decode(encoding='GBK'))
print(byte2.decode(encoding='UTF-8'))