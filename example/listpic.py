#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

L = list(range(100))
print L
print L[:10]
print L[-10:]
print L[10:20]
print L[:10:2]
print L[::5]
print L[:]

print (0, 1, 2, 3, 4, 5)[:3]

print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]


#迭代
from collections import Iterable

print isinstance('abc', Iterable) # str是否可迭代
print isinstance([1, 2, 3], Iterable) # list是否可迭代
print isinstance(123, Iterable) # 整数是否可迭代

for i, value in enumerate(['A', 'B', 'C']):
    print (i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print (x, y)

#列表生成器
print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]
print [m + n for m in 'ABC' for n in 'XYZ']


#测试
import os  # 导入os模块，模块的概念后面讲到

print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录

print L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]


#生成器
g = (x * x for x in range(10))
print g

print next(g)
print next(g)
