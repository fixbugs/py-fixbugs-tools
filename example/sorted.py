#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

print sorted([36, 5, -12, 9, -21])
print sorted([36, 5, -12, 9, -21], key=abs)

print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


#lazy sum functions
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print f = lazy_sum(1, 3, 5, 7, 9)

print f1 = lazy_sum(1, 3, 5, 7, 9)
print f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 = f2


#count sth
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print f1()
print f2()
print f3()


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))# f(i)立刻被执行，因此i的当前值被传入f()
    return fs

print f1()
print f2()
print f3()


print list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
