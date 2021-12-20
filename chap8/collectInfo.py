# -*- coding:utf-8 -*-
# @Time : 2021/12/20 9:30 PM
# @Author: jonas.jiang
# @File : collectInfo.py
print('---------------  judge  ----------------')
s1 = {1, 2, 4, 4}
s2 = {1, 2, 4, 4}
print(s1 == s2)
print(s1 != s2)

print('--------------- s1 是否是 s2 的子集   ----------------')
print(s1, s2)
s1.add(55)
print(s1.issubset(s2))
# print(s2.issubset(s1))

print('--------------- s1 是否是 s2 的超集   ----------------')
print(s1.issuperset(s2))
# print(s2.issuperset(s1))

print('--------------- 两个集合是否有交集：没有：true 有：false   ----------------')
print(s1.isdisjoint(s2))

print('---------------  数学-交集  ----------------')
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.intersection(s2))
print(s1 & s2)
print(s1, s2)

print('---------------  数学-并集  ----------------')
print(s1.union(s2))
print(s1, s2)

print('---------------  数学-差集  ----------------')
print('s1的差集', s1.difference(s2))
print('s2的差集', s2.difference(s1))
print(s1, s2)

print('---------------  数学-对称差集  ----------------')
print(s1 ^ s2)
