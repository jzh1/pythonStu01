# -*- coding:utf-8 -*-
# @Time : 2021/12/23 10:29 PM
# @Author: jonas.jiang
# @File : function2.py
def fun(al):
    old = []
    new = []
    for i in al:
        if i % 2:
            old.append(i)
        else:
            new.append(i)

    return old, new

print('--------------- 没有返回值可以不写return   ----------------')
print('--------------- 返回值一个，直接返回该类型   ----------------')
print('--------------- 返回值二个，是元组   ----------------')
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(fun(li))
