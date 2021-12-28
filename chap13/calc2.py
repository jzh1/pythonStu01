# -*- coding:utf-8 -*-
# @Time : 2021/12/28 11:53 PM
# @Author: jonas.jiang
# @File : calc.py
def add(a, b):
    return a + b

# 只有当作主程序时才会执行，被引入时不会执行
if __name__ == '__main__':
    print(add(100, 2))
