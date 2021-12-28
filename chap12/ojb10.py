# -*- coding:utf-8 -*-
# @Time : 2021/12/28 11:29 PM
# @Author: jonas.jiang
# @File : ojb10.py



class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = Cpu
        self.disk = disk


cpu1 = Cpu()
cpu2 = cpu1
print('--------------- cpu1变量赋值   ----------------')
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))
print('---------------  disk1  ----------------')
disk1 = Disk()
print(disk1, id(disk1))
print('--------------- 浅拷贝(只copy实例对象)   ----------------')
computer = Computer(cpu1, disk1)

import copy

computer1 = copy.copy(computer)
computer2 = copy.deepcopy(computer)
print('---------------  原对象  ----------------')
print(computer, computer.cpu, computer.disk)
print('---------------  浅拷贝  ----------------')
print(computer1, computer1.cpu, computer1.disk)
print('---------------  深拷贝  ----------------')
print(computer2, computer2.cpu, computer2.disk)
