#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

print ('包含中文的str')
print ord('A')
print ord('中')
print chr(66)
print chr(25591)

print '\u4e2d\u6587'

x = b'ABC'
print x

print 'ABC'.encode('ascii')
print '中文'.encode('utf-8')

print b'ABC'.decode('ascii')
print b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#%d int %f float %s string %x 16进制
print 'Hi, %s, you have $%d.' % ('Everybody', 100000000)

#小数点
print '%.2f' % 3.1415926
