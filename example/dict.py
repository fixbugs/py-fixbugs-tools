#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d
print d['Bob']
d['Jack'] = 90
print d

print 'Thomas' in d
print 'Bob' in d

print d.get('Thomas')
print d.get('Thomas', -1)

d.pop('Bob')
print d


# set

s = set([1, 2, 3])
print s

s = set([1, 1, 2, 2, 3, 3])
print s

s.add(4)
print s

s.remove(4)
print s


s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2

print s1 | s2

a = ['c', 'b', 'a']
print a
a.sort()
print a

a = 'abc'
print a.replace('a', 'A')
print a

a = 'abc'
b = a.replace('a', 'A')
print b
print a
