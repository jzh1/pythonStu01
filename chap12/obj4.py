# -*- coding:utf-8 -*-
# @Time : 2021/12/27 10:49 PM
# @Author: jonas.jiang
# @File : obj4.py

class Student:
    def __init__(self):
        pass

    # 重写
    def __str__(self):
        return '我的student类{0}'.format(1)


stu = Student()
print(dir(stu))
print('对象的描述')
print(stu.__str__())

