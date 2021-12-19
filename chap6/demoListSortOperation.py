# -*- coding:utf-8 -*-
# @Time : 2021/12/19 下午11:40
# @Author: jonas.jiang
# @File : demoListOperation.py

# add an element to the end of the list
lst = [99, 33, 11, 12, 34]
print(lst)
# 原列表排序
print('---------------  原列表排序  ----------------')
lst.sort()
print(lst)
# 升序
lst.sort(reverse=False)
print(lst)
# 降序
lst.sort(reverse=True)
print(lst)
lst1 = [99, 33, 11, 12, 34]
print('---------------  sorted内置排序函数，默认升序,重新生成列表,原列表没有任何改变  ----------------')
print(id(lst1))
lst2 = sorted(lst1, reverse=True)
print(id(lst1))

