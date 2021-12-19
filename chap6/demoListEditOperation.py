# -*- coding:utf-8 -*-
# @Time : 2021/12/19 下午11:40
# @Author: jonas.jiang
# @File : demoListOperation.py

# edit list value
lst = [11, 12, 34,55,66,77]
print(lst)
lst[1] = 99
print(lst)
print('---------------  切片索引1,2 替换为...  ----------------')
lst[1:3] = ['hello','lo','iii','qqq']
print(lst)