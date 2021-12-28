# -*- coding:utf-8 -*-
# @Time : 2021/12/28 11:40 PM
# @Author: jonas.jiang
# @File : demo1.py
# python 解释器相关的
import sys
# 时间相关的
import time
# 操作系统服务
import os
# 日期
import calendar
# 服务器数据
import urllib.request
# json
import json
# 正则
import re
# 数学
import math
# 精确数学
import decimal
# 日志
import logging

print('---------------  sys  ----------------')
print(sys.getsizeof(24))
print(sys.getsizeof(240))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print('---------------  time  ----------------')
print(time.time())
print(time.localtime(time.time()))
print(time.asctime())
print('---------------  urllib  ----------------')
response = urllib.request.urlopen('http://www.baidu.com/').read()
print(response)
print('---------------  math  ----------------')
print(math.pi)