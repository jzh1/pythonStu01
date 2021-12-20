# -*- coding:utf-8 -*-
# @Time : 2021/12/20 8:25 PM
# @Author: jonas.jiang
# @File : createAngGet.py
print('--------------- two create function   ----------------')
score = {'jzh': 199, 'lili': 123, 'xiaoming': 12}
score2 = dict(name='lili', age=111)
print(score)
print(score2)

print('---------------  get  function   ----------------')
# is not set :KeyError
print(score['jzh'])
# is not set : none
print(score.get('lili'))
# is not set : set default
print(score.get('maqi', 99))
