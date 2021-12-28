# -*- coding:utf-8 -*-
# @Time : 2021/12/29 12:53 AM
# @Author: jonas.jiang
# @File : demo4.py
class MyCount(object):
    def __enter__(self):
        print('__enter__ 被执行')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ 被执行')

    def show(self):
        print('show 被执行')


with MyCount() as file: # file 相当于MyCount，无论是否会产生异常都会调用__exit__
    file.show()
