# -*- coding:utf-8 -*-
# @Time : 2021/12/29 12:20 AM
# @Author: jonas.jiang
# @File : demo6.py
import time

import schedule


def job():
    print('---哈哈哈')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
