# -*- coding:utf-8 -*-
# @Time : 2021/12/25 上午11:37
# @Author: jonas.jiang
# @File : bug1.py
import traceback

try:
    print('----------------------------------')
    print(10 / 0)
except:
    traceback.print_exc()

print('------------------ bug 的由来 ----------------')
# 马克2号，调试时被一只阻碍

print('------------------ bug 的由来 ----------------')
print('------------------ 常见的错误类型 ----------------')
print('ZeroDivisionError 数学运算错误')
print('IndexError')
print('KeyError')
print('NameError 为定义名字')
print('SyntaxError 语法错误')
print('ValueError 值错误')

print('------------------ try except ----------------')
try:
    a = int(input("place input num : "))
    c = 2 / a
    re = c
except ValueError as e:
    print('ZeroDivisionError出错了', e)
except BaseException as e:
    print('ZeroDivisionError出错了', e)
else:
    print('else 没出正确执行', re)
finally:
    print('不管正确与都会执行')






