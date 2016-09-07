#!/usr/bin/env python
#coding=utf-8

cacheFileName = 'cache.data'


def write_file(offset, bytestr):
    f = file(cacheFileName, 'wb+')
    f.seek(offset)
    f.write(bytestr)
    f.close()

import os


def read_file(offset, length):
    if not os.path.exists(cacheFileName):
        return list()
    f = file(cacheFileName, 'rb+')
    f.seek(offset)
    res = f.read(length)
    f.close()
    return res

mp = {}


# user_code
def get(key):
    key = createNewKey(key)
    return heightToInt(mp.get(key, 0))


def put(key):
    key = createNewKey(key)
    last_num = heightToInt(str(mp.get(key, '0')))
    mp[key] = intToHeight(last_num + 1)
    s = ''
    for kv in mp.items():
        s = '%s:%s\n' % kv + s
    b_s = bytearray(s)
    write_file(0, b_s)


def init():
    #ls = map(chr, read_file(0, 102400))
    ls = read_file(0, 102400)
    for li in ''.join(str(v) for v in ls).split('\n'):
        l2 = li.split(':')
        if len(l2) < 2:
            continue
        mp[l2[0]] = str(l2[1])


def createNewKey(key):
    if len(key) < 8 :
        return key
    import hashlib
    hash_key = hashlib.md5(key).hexdigest()
    result = hash_key[0:8]
    return result


def intToHeight(num):
    loop = '0123456789abcdefghijklmnopqrstuvwxyz'
    a = []
    while num != 0:
        a.append(loop[num % 36])
        num = num / 36
    a.reverse()
    return ''.join(a)


def heightToInt(nstr):
    nstr = str(nstr)
    loop = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = 0
    length = len(nstr)
    for i in range(length)[::-1]:
        res += loop.index(nstr[i]) * pow(36, length-i-1)
    return res


def getRandomStr(length):
    import random
    main_str = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()'
    return ''.join(random.sample(main_str, int(length)))

if __name__ == '__main__':
    # error on key 89,need 1, but output 0
    slist = list()
    init()
    for i in range(0, 200):
        tmp = getRandomStr(18)
        slist.append(tmp)
        put(str(tmp))
    for i in range(0, 200):
        print get(slist[i])
    print get('89')
    exit(0)
    init()
    keys = ['89', 'test2', 'test3','sjflksjfljsldjf','weewerwerwer','werwnkashfhshdfk']
    for k in keys:
        put(k)
    for k in keys:
        print get(k)
