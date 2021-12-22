# -*- coding:utf-8 -*-
# @Time : 2021/12/21 9:58 PM
# @Author: jonas.jiang
# @File : get.py
s = 'helo helo'
# 查不到会抛出异常
print(s.index('lo'))
# 查不到不会抛出异常 -1
print(s.find('lo'))

print(s.rindex('lo'))
print(s.rfind('lo'))

print('--------------- string 大小写转换 function   ----------------')
print(s)
print('转换为大写',s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

print('--------------- string 左对齐 function   ----------------')
s1 = 'hello,python'
print(s1.center(20,'*'))
print(s1.ljust(20,'*'))
print(s1.ljust(10))
print(s1.ljust(20))

print('--------------- string 右对齐 function   ----------------')
print(s1.rjust(10))
print(s1.rjust(20,'*'))
print(s1.rjust(20))
print('---------------    ----------------')
print(s1.zfill(20))
