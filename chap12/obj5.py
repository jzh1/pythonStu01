# -*- coding:utf-8 -*-
# @Time : 2021/12/27 10:49 PM
# @Author: jonas.jiang
# @File : obj4.py

class Animal:
    def eat(self):
        print('动物吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃屎')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(Animal):
    def eat(self):
        print('人吃食物')


def fun(ojb):
    ojb.eat()

print('---------------  原始实现效果  ----------------')
cat = Cat()
dog = Dog()
person = Person()
cat.eat()
dog.eat()
person.eat()

print('---------------  多态  ----------------')
fun(Cat())
fun(Dog())
fun(Person())
