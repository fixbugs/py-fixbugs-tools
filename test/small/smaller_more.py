#!/usr/bin/env python
#coding=utf-8

import hashlib

def string_md5(c_str):
    return hashlib.md5(c_str).hexdigest()

def wheelerTransform(data):
    data = "^" + data + "|"
    length = len(data)
    rotations = []
    for i in range(length, 0, -1):
        rotations.append(data[i:length] + data[0:i])
    rotations.sort()
    result = ""
    for r in rotations:
        result += r[length - 1]
    return result

def getFileContent(file_path):
    import os
    if not os.path.exists(file_path):
        return False
    result = []
    try:
        f = open(file_path, 'r')
        result = f.readlines()
    finally:
        f.close()
    return result

def compress(data):
    result = ""
    count = 1
    cur = data[0]
    for d in data[1:]:
        if(d != cur):
            result += cur + str(count)
            count = 1
            cur = d
        else:
            count += 1
    return result + cur + str(count)


def bwt(string, slice_len):
    string_len = len(string)
    string_slice = []
    for index in range(len(string)):
        s, e = index, (index+slice_len) % string_len
        if s < e:
            string_slice.append((string[s:e], string[s-1]))
        else:
            string_slice.append((string[s:] + string[:e], string[s-1]))
    return string_slice

if __name__ == '__main__':
    sstr = getFileContent('war_and_piece.txt')
    # #print wheelerTransform("BABABABANANABABABABABANANABABABABABANANABANANANAAHH")
    # bwt_res = bwt(sstr[0], 100)
    # bwt_res = sorted(bwt_res)
    # bwt_res = bwt_res[0:10]
    # #print bwt_res
    # nw = list()
    # #b2 = list()
    # for b in bwt_res:
    #  #   b2.append(b[1])
    #     print b[0]
    #     tmp = wheelerTransform(b[0])
    #     nw.append(tmp)
        #print tmp
    wt = wheelerTransform(sstr)
    #b2 = sorted(b2)
    #wt = wheelerTransform(''.join(b2) )
    print wt
    #wt = ''.join(nw)
    print '-----wt-----------'
    print '---------md5---result------'
    print string_md5(wt)
