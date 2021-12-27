# -*- coding:utf-8 -*-
# @Time : 2021/12/27 10:10 PM
# @Author: jonas.jiang
# @File : obj1.py

class Car:
    def __init__(self, name, age=12):
        self.name = name
        # 不希望在外部使用所以使用__，但是可以通过 _类名__age使用 示例：_Car__age
        self.__age = age

    def get_name(self):
        print('汽车型号：' + self.name)

    def get_age(self):
        print('汽车使用年龄：' + str(self.__age))

    def show(self):
        print('汽车型号：' + self.name + ',汽车使用年龄：' + str(self.__age))


car = Car('宝马X5')
car.get_name()
car.show()
print(car.name)
print(dir(car))
# 输出：['_Car__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_age', 'get_name', 'name', 'show']

print(car._Car__age)
