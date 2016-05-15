#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-


def my_abs(x):
    #if not isinstance(x, (int, float)):
    #    raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-2000)
print my_abs('A')


import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print (x, y)

r = move(100, 100, 60, math.pi / 6)
print r


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(2)
print power(2, 3)


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


#test

def add_end(L=[]):
    L.append('END')
    return L


print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])
print add_end()
print add_end()
print add_end()


def new_add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print new_add_end()
print new_add_end()
print new_add_end()
print new_add_end()


#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1, 2, 3)
print calc(1, 3, 5, 7)


def new_calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print new_calc(1, 2)
print new_calc()

nums = [1, 2, 3]
print new_calc(nums[0], nums[1], nums[2])

print calc(*nums)


#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print person('Michael', 30)
print person('Bob', 35, city='Beijing')
print person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack', 24, **extra)


#new test
def newperson(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

print newperson('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


#限制关键字参数，只接收ciyt和job
def nnewperson(name, age, city, job):
    print(name, age, city, job)

print nnewperson('Jack', 24, city='Beijing', job='Engineer')
print nnewperson('Jack', 24, 'Beijing', 'Engineer')


#参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print f1(1, 2)
print f1(1, 2, c=3)
print f1(1, 2, 3, 'a', 'b')
print f1(1, 2, 3, 'a', 'b', x=99)
print f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print f2(*args, **kw)
