#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

print int('12345')

print int('12345', base=8)

print int('12345', 16)


def int2(x, base=2):
    return int(x, base)

print int2('1000000')
print int2('1010101')


import functools

int2 = functools.partial(int, base=2)

print int2('1000000')
print int2('1010101')

print int2('1000000', base=10)

max2 = functools.partial(max, 10)

print max2(5, 6, 7)

#args = (10, 5, 6, 7)
#print max(*args)

