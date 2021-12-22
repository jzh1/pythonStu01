# -*- coding:utf-8 -*-
# @Time : 2021/12/22 9:46 PM
# @Author: jonas.jiang
# @File : splitString.py
s = 'helo ｜helo ｜python'
print('--------------- 左侧批分   ----------------')
print(s.split())
print(s.split(' ', maxsplit=1))
print(s.split('|'))
print(s.split('|', maxsplit=1))

print('--------------- 右侧批分   ----------------')
print(s.rsplit())
print(s.rsplit(' ', maxsplit=1))
print(s.rsplit('|'))
print(s.rsplit('|', maxsplit=1))