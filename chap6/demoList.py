# -*- coding:utf-8 -*-
# @Time : 2021/12/18 下午1:27
# @Author: jonas.jiang
# @File : demoList.py
# 列表存储的是引用（id）,并不是具体的值

# 创建列表，有序的,可以存储重续的数据
# from operator import index

list0 = ['hello', 'world', 98, 99, 19, 80]
list1 = ['hello', 'world', 98]
list2 = list([1, 2, 3, 4, '21323'])

print('---------- 有两个索引的，正数索引和负数索引 -------------------')
print('---------- 根据索引输出值 -------------------')
print(list2[0])

# 获取索引(有相同值，只返回第一个)
print('---------- 输出值的索引 -------------------')
print(list1, list0.index(98))

print('---------- 输出值的索引（指定位置） -------------------')
print(list0.index(98, 1, 3))

print('---------- 获取元素 -------------------')
print(list0[1], list0[-1])
