# -*- coding:utf-8 -*-
# @Time : 2021/12/20 9:16 PM
# @Author: jonas.jiang
# @File : collect.py
print('---------------  judge  ----------------')
co = {1, 2, 4, 44, 44}
print(1 in co)
print(1 not in co)

print('---------------  add (one) ----------------')
co.add(12)
print(co)

print('---------------  update (batch) ----------------')
co.update([11, 22, 44])
co.update((1, 2, 3))
co.update({'ppop', '23dd'})
print(co)

print('---------------  remove  ----------------')
co.remove(11)  # 抛异常
co.discard(600)  # 不会抛异常
co.pop()  # 随机删除
print(co)

co.clear() # 清空
print(co)
