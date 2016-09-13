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
    #todo 无损压缩
    b_s = lzw_encode(b_s)
    #需要计算并定位需要修改或者写入的字符内容
    write_file(0, b_s)


def init():
    #ls = map(chr, read_file(0, 102400))
    ls = read_file(0, 102400)
    if ls:
        ls = lzw_decode(ls)
    for li in ''.join(str(v) for v in ls).split('\n'):
        l2 = li.split(':')
        if len(l2) < 2:
            continue
        mp[l2[0]] = str(l2[1])


def createNewKey(key):
    if len(key) < 8:
        return key
    import hashlib
    hash_key = hashlib.md5(key).hexdigest()
    hash_key = hashlib.md5(hash_key + key).hexdigest()
    result = hash_key[0:2]
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


def LZW(inStr, narrow=False, bits=14):
    '''''使用LZW压缩算法压缩。
        narrow为True时输出字节流位紧缩
        默认最大位宽14位，允许范围12~16位'''
    if isinstance(inStr, str):
        inStr = list(inStr)
        for i in range(len(inStr)):
            inStr[i] = ord(inStr[i])
    sOutStr = [256]   # 先放一个 开始&清除 标记
    mTagMap = {}      # 字典
    iTagCurrent = 258  # 当前的标记总数 0~255 标记256 为begin & clear , 257 为end
    iBitsLen = 9
    iTag = inStr[0]   # 当前标记
    ii = 0
    cTemp = 0
    if bits > 16 or bits < 12:
        return None
    iMaxLen = (1 << bits)-1   # 最多允许的标记数，由位宽决定

    for ii in range(1, len(inStr)):
        cChar = inStr[ii]
        cTemp = (iTag << 8)+cChar   # （前缀 后缀）
        if cTemp in mTagMap:    # 该（前缀 后缀）已存在
            iTag = mTagMap[cTemp]  # 取出其标记
        else:   # 不存在
            sOutStr.append(iTag)  # 将前缀放入输出流
            mTagMap[cTemp] = iTagCurrent
            iTagCurrent += 1      # 增加一个标记，并放入字典
            iTag = cChar  # 当前标记为后缀

        if iTagCurrent >= iMaxLen:    # 如果到达了最大标记数，清除字典，从头开始
            sOutStr.append(256)
            mTagMap = {}
            iTagCurrent = 258

    if iTag != 0:
        sOutStr.append(iTag)
    sOutStr.append(257) # 放入结束标记

    if narrow:  # 位紧缩
        return Narrow(sOutStr)
    else:
        return sOutStr


def Narrow(sOutStr):
    sOutN = []
    iTemp = 0
    BitLeft = 0
    nowBit = 9  # 当前位宽
    nowStag = 1 << nowBit  # 当前位宽允许的标记数
    nowTagCount = 258
    for cChar in sOutStr:
        iTemp = iTemp+(cChar << BitLeft)
        nowTagCount += 1
        BitLeft += nowBit

        if cChar == 256:
            nowBit = 9
            nowStag = 1 << nowBit
            nowTagCount = 258

        if nowTagCount >= nowStag:
            nowBit += 1
            nowStag = 1 << nowBit

        while BitLeft >= 8:
            sOutN.append(iTemp & 0xff)
            iTemp = iTemp >> 8
            BitLeft -= 8
    if BitLeft > 0:
        sOutN.append(iTemp)
    return sOutN


def UnNarrow(inStr):
    sOut = []
    iTemp = 0
    BitLeft = 0
    nowBit = 9
    nowStag = 1 << nowBit
    mask = nowStag-1
    nowTagCount = 258
    for cChar in inStr:
        iTemp = iTemp+( cChar << BitLeft)
        BitLeft += 8
        if BitLeft >= nowBit:
            cTemp = iTemp & mask
            iTemp = iTemp >> nowBit
            BitLeft -= nowBit
            sOut.append(cTemp)
            nowTagCount += 1
            if nowTagCount >= nowStag:
                nowBit += 1
                nowStag = 1 << nowBit
                mask = nowStag-1
            if cTemp == 256:
                nowBit = 9
                nowStag = 1 << nowBit
                mask = nowStag-1
                nowTagCount = 258
    if BitLeft > 0:
        sOut.append(iTemp)

    return sOut


def deTag(mTagMap, nowTag, outStr):
    '''''将一个标记转化为元字符序列，并放入到输出流中'''
    if nowTag >= 0:
        sTemp = []
        while nowTag > 255:
            pair = mTagMap[nowTag]
            sTemp.append(pair[1])
            nowTag = pair[0]
        sTemp.append(nowTag)
        sTemp.reverse()
        outStr += sTemp
    return nowTag


def UnLZW(inStr, narrow=False):
    if narrow:
        inStr = UnNarrow(inStr)

    mTagMap = {}
    outStr = []
    nowTagCount = 258
    sTemp = []
    nowTag = -1
    for cChar in inStr:
        if cChar == 256:
            if nowTag >= 0:
                deTag(mTagMap, nowTag, outStr)
            mTagMap = {}
            nowTagCount = 258
            nowTag = -1
        elif cChar == 257:
            if nowTag >= 0:
                deTag(mTagMap, nowTag, outStr)
                nowTag = -1
            return outStr
        elif nowTag == -1: #刚开始
            nowTag = cChar
        else:
            pair = [nowTag, 0]
            mTagMap[nowTagCount] = pair
            nowTagCount += 1
            surfix = cChar
            while surfix > 255:
                if surfix not in mTagMap:
                    print 'Thera are errors in input'
                    return outStr
                surfix = mTagMap[surfix][0]
            pair[1] = surfix
            deTag(mTagMap, nowTag, outStr)
            nowTag = cChar


def lzw_encode(estr):
    estr = LZW(estr, True, 16)
    eouts = ''
    for d in estr:
        eouts += chr(d)
    return eouts


def lzw_decode(dstr):
    ll = list()
    for s in dstr:
        ll.append(ord(s))
    destr = UnLZW(ll, True)
    outs = ''
    for d in destr:
        outs += chr(d)
    return outs

if __name__ == '__main__':
    #test write
    # error on key 89,need 1, but output 0
    slist = list()
    init()
    for i in range(0, 400):
        tmp = getRandomStr(18)
        slist.append(tmp)
        put(str(tmp))
    # for i in range(0, 200):
    #     print get(slist[i])
    print get('89')
    exit(0)
    init()
    keys = ['89', 'test2', 'test3', 'sjflksjfljsldjf', 'weewerwerwer', 'werwnkashfhshdfk']
    for k in keys:
        put(k)
    for k in keys:
        print get(k)
