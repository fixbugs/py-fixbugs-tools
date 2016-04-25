#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

print 'abc', type('abc')
print 'ab1', type('ab1')
print '123', type('123')
print 123, type(123)
print '1ab', type('1ab')
print [1,2], type([1,2])
print {'1':1}, type({'1':1})
print True, type(True)
print None,type(None)

print '---------continue-------------'
exit(0)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print n
print f
print s1
print s2
print s3
print s4
