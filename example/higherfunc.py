#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

print list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


from functools import reduce


def add(x, y):
    return x + y

print reduce(add, [1, 3, 5, 7, 9])


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn, map(char2num, '13579'))


import itertools


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = itertools.ifilter(_not_divisible(n), it) # 构造新序列


#prime = filter(lambda x: not [x % i for i in range(2, x) if x % i == 0], range( 2, 101))
#print prime

for n in primes():
    if n < 1000:
        print n
    else:
        break
