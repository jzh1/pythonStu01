# -*- coding:utf-8 -*-
# @Time : 2021/12/22 9:53 PM
# @Author: jonas.jiang
# @File : stringJust.py
print('---------------  判断是否是合法字符串   ----------------')
print('dsfsf'.isidentifier())

print('---------------  判断是否是空白制表符回车组成   ----------------')
print('  '.isspace())
print(' dsf '.isspace())
print(' \t  '.isspace())

print('--------------- all 字母组成   ----------------')
print('qwed'.isalpha())

print('--------------- all 数字   ----------------')
print('sdfs'.isdecimal())
print('123'.isdecimal())

print('--------------- all 数字   ----------------')
print('123'.isnumeric())

print('--------------- all 数字字母   ----------------')
print('123123mmsmdf'.isalnum())
print('123'.isalnum())
print('mkk'.isalnum())