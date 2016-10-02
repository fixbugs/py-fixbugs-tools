#!/usr/bin/env python
#coding=utf8
#need change for used
filePathIP = '/Users/fuxin/test/ip/taobaoip/ip.data'

f = open(filePathIP, 'r')
d = f.read()
f.close()
a = {}
for i in range(0, len(d), 5):
    t = ord(d[i+2])*256+ord(d[i+3])
    if t in a:
        a[t] += 256
    else:
        a[t] = 256

print a
print a[133], 'sh'
print a[242], 'hz'
print a[29], 'bj'
print a[75], 'sz'
print a[242], ',', a[29], ',', a[133], ',', a[75]
exit(0)
#print "上海："+str(a['上海'])
