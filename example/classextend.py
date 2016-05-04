#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Husky(Dog):
    pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = Animal()
d = Dog()
h = Husky()

print isinstance(h, Husky)
print isinstance(h, Dog)
print isinstance(h, Animal)
print isinstance(d, Dog) and isinstance(d, Animal)

print dir('ABC')
print dir(Husky)
