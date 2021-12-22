# -*- coding:utf-8 -*-
# @Time : 2021/12/22 10:20 PM
# @Author: jonas.jiang
# @File : format.py
print('---------------  %s string'
      ' %i or %d 整数'
      '%f 浮点数  '
      '{} 占位符----------------')
name = 'jzh'
age = 11
print('---------------  三种格式化方法   ----------------')
# 1
print('我叫%s今年%d岁了' % (name, age))
# 2
print('我叫{0},今年{1}岁了,我叫{0}'.format(name, age))
# 3
print(f'我叫{name},今年{age}岁了,我叫{name}')
print('---------------  % d  ----------------')
# 10 是宽度，所有一共是十个宽度
print('%10d' % 99)
print('%1d' % 99)
print('%2d' % 99)
print('%3d' % 99)
print('1234567890')

print('---------------  % f  ----------------')
# .3 小数保留三位
print('%.3f' % 99.123456)
# .3 小数保留三位,6 宽度
print('%10.3f' % 99.123456)

print('---------------  format  ----------------')
# .3 表示一共三位数
print('{0:.3}'.format(3.14159))
# .3f 表示三位小数
print('{0:.3f}'.format(3.14159))
# 10是宽度 .3f表示三位小数
print('{0:10.3f}'.format(3.14159))