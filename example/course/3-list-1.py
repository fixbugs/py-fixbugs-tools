#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

# classmates = ['Michael', 'Bob', 'Tracy']
# print classmates

# print dir(classmates)

# print len(classmates)

# print classmates[0]

# print classmates[-1]

# classmates.append('Adam')
# print classmates

# classmates.insert(1, 'Jack')
# print classmates

# print classmates.pop()
# print classmates

# print classmates.pop(1)
# print classmates

# classmates[1] = 'Sarah'
# print classmates

# L = ['apple', 123, True]
# print L, len(L)

s = ['a', 'b', ['c', 'd'], 'e']
print s, len(s)


#tuple
t = (1, 2)
print t

t = ()
print t

t = (1,)
print t

t = ('a', 'b', ['A', 'B'])
print t
t[2][0] = 'X'
t[2][1] = 'Y'
print t


#按相反的顺序输出列表值
a = ['one', 'two', 'three']
for i in a[::-1]:
    print i
