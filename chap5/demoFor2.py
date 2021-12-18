# -*- coding:utf-8 -*-
# @Time : 2021/12/18 下午12:43
# @Author: jonas.jiang
# @File : demoFor2.py
# break 停止循环
# continue 跳出本次循环
# else 可以搭配for,while 使用，只要中间没有被break就会触发else
print('--------------- break  ---------------')
for item in range(3):
    pwd = int(input('请输入密码:'))
    if pwd == 888:
        print('密码正确')
        break
    else:
        print('pwd error,place re-enter')
else:
    print("maximum number of error reached ")

print('--------------- continue  ---------------')
#...
