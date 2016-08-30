#!/usr/bin/env python
#coding=utf-8

def encode(num):
    rstr = str(num)
    nlen = len(rstr)
    nstr = ''
    if nlen < 10:
        nstr = '0' + str(nlen)
    else:
        nstr = str(nlen)
    rstr = str(nstr) + rstr
    return rstr


def decode(rstr):
    nlen_str = rstr[0:2]
    nstr = rstr[2:]
    num = int(nstr)
    return num


if __name__ == '__main__':
    nlist = [0,8,9,10,18,19]
    for n in nlist:
        print '-------start--------'
        e_r = encode(n)
        print 'encode result:',e_r
        d_r = decode(e_r)
        print 'decode result:',d_r
        print 'num in:',n
        if n == d_r:
            print 'success'
        else:
            print 'failed,num', n
            break
        print '--------end------'
