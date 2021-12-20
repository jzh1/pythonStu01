# -*- coding:utf-8 -*-
# @Time : 2021/12/20 9:48 PM
# @Author: jonas.jiang
# @File : String.py
print('---------------  驻留是在交互窗口中 create 符合标识符的（字母，数字，下划线）字符串相同，公用内存地址 ----------------')
s1 = 'hello world'
s2 = "hello world"
s3 = '''hello world'''
print(id(s1), id(s1), id(s3))

s4 = 'abc%'
s5 = 'abc%'
print(id(s4), id(s5))
