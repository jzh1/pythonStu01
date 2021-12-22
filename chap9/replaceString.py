# -*- coding:utf-8 -*-
# @Time : 2021/12/22 9:58 PM
# @Author: jonas.jiang
# @File : replaceString.py
print('---------------  替换  ----------------')
s = 'hello python'
print(s)
sre = s.replace('python', 'java')
s1 = 'hello python hello python hello python'
sre1 = s1.replace('python', 'java', 2)
print(sre1)

print('--------------- 替换为指定类型 .join   ----------------')
sl = ['hello', 'java', 'python']
sl1 = ('hello', 'java', 'python')
print('｜'.join(sl))
print(' '.join(sl))
print(','.join(sl))

print(','.join(sl1))
print('*'.join(s))
