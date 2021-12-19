# -*- coding:utf-8 -*-
# @Time : 2021/12/19 下午11:40
# @Author: jonas.jiang
# @File : demoListOperation.py

# add an element to the end of the list
lst = [11, 12, 34]
lst.append(1)
print(lst)

# # add an element to the start of the list
lst2 = [11, 12, 34]
lst2.append(lst)
print(lst2)
# Add at least one element at the end of the list
lst2.extend(lst)
print(lst2)
# Add an element anywhere in the list
lst3 = [1, 2, 4, 5]
lst3.insert(99, 66)
print(lst3)

print('---------------  切片  ----------------')
lst5 = [1,2,3,4,5,6,7]
lstStr = ['hello','world']
# 从第一个开始截断替换
lst5[1:] = lstStr
print(lst5)