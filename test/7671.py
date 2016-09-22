#!/usr/bin/env python
#coding=utf8

import simplejson


def getdata(url):
    import urllib2
    req = urllib2.Request(url=url)
    soc = urllib2.urlopen(req)
    con = soc.read()
    soc.close()
    return simplejson.loads(con)


base_num = 46364

url = 'http://www.qlcoder.com/train/mysql?table=5&a=46364&b=100'
#d = getdata(url)

baseu = 'http://www.qlcoder.com/train/mysql?&b=100&a='

# result = list()

# turll = list()
# for i in range(0, 10):
#     now_table_name = str(i)
#     for j in range(0, 6):
#         turl = baseu + str(base_num+(j*100)) + '&table=' + now_table_name
#         tres = getdata(turl)
#         print tres['data']
#         result.extend(tres['data'])
#     print now_table_name
# print '--------------------------------'
# print len(result)

cacheFileName = 'datag.data'

import os


def write_file(offset, bytestr):
    f = file(cacheFileName, 'wb+')
    f.seek(offset)
    f.write(bytestr)
    f.close()


def read_file(offset, length):
    if not os.path.exists(cacheFileName):
        return list()
    f = file(cacheFileName, 'rb+')
    f.seek(offset)
    res = f.read(length)
    f.close()
    return res

# dataString = simplejson.dumps(result)

# write_file(0, dataString)




fdatas = read_file(0, 102400000)
all_data = simplejson.loads(fdatas)
print type(all_data)
print all_data[0]
print all_data[1]
print '-----------'
all_data.sort(lambda x,y:cmp(x['favs'],y['favs']) )
all_data.reverse()
print all_data[2999]
print all_data[3000]

st_num = 2999+1
ssum = 0
for i in range(0, 20):
    ssum += all_data[st_num+i]['favs']
print ssum
