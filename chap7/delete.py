# -*- coding:utf-8 -*-
# @Time : 2021/12/20 8:25 PM
# @Author: jonas.jiang
# @File : createAngGet.py
print('--------------- judge function   ----------------')
score = {'jzh': 199, 'lili': 123, 'xiaoming': 12}
score2 = dict(name='lili', age=111)
print('jzh' in score)
print('jzh' not in score)

print('--------------- del and clear function   ----------------')
del score['jzh']
print(score)
score.clear()
print(score)

print('--------------- update function   ----------------')
score['jzh'] = 1000
print(score)