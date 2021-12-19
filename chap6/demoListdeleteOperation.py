# -*- coding:utf-8 -*-
# @Time : 2021/12/19 下午11:40
# @Author: jonas.jiang
# @File : demoListOperation.py

#
lst = [11, 12, 34,66,77,88,99]
print(lst)
# 根据值移除
lst.remove(11)
print(lst)
# 根据索引移除-- 指定的索引不存在报错，
lst.pop(1)
# 默认删除最后一个
lst.pop()
print(lst)

# 切片
print('---------------  切片1,2  ----------------')
lst1 = [11, 12, 34,66,77,88,99]
new_list = lst1[1:3]
print(lst1,new_list)
# 删除切片的值（不是删除，但是用替换实现了删除的效果）
lst1[1:3] = []
print(lst1)

print('---------------  清空  ----------------')
lst1.clear()
print(lst1)

print('---------------  删除列表对象（打印会报错） ----------------')
del lst1
# print(lst1)