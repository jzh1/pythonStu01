# -*- coding:utf-8 -*-
# @Time : 2021/12/30 11:36 PM
# @Author: jonas.jiang
# @File : demo1.py
num = int(input('place input number:'))
print(num, '的二进制是：', bin(num))
print(num, '的八进制是：', oct(num))
print(num, '的十六进制是：', hex(num))
print(str(num) + '的二进制是：' + bin(num))
print(f'{num}的二进制是:{bin(num)}')
print('{0}的二进制是:{1}'.format(num, bin(num)))
