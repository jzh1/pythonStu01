# -*- coding:utf-8 -*-
# @Time : 2021/12/22 10:07 PM
# @Author: jonas.jiang
# @File : compare.py
print('--------------- 从左往右比较 阿斯卡吗值,原始值   ----------------')
s = '123456789abcdefg'
s1 = 'wqwe'
print(s > s1)
print('apple' > 'app')
print('apple' > 'blan')
print('apple' < 'blan')

print(chr(98), chr(99))

print('---------------  切片[start:end:step] start-default:o end-default:end step:1  ----------------')
s2 = s[:5]
print(s2)
print(s[5:])
print(s[5:12])
print(s[5::2])
print(s[-5:])