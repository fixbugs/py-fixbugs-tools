#!/usr/bin/env python
#coding=utf8


n_str = '14a091645d307b8abd8632a1fb83f81e38c1b33d3286ca814a5742bec52c4b06d08'

ten_str = int(n_str, 16)

def calc(num, exp, mod):
    """快速幂"""
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    elif exp % 2 == 0:
        return (calc(num, exp/2, mod)**2)%mod
    else:
        return (calc(num, exp/2, mod)**2*num)%mod

des_ten_str = calc(ten_str, 65537, long('41031587223377599579245988781518671358060455361860183212406274189493280555347897') )

print des_ten_str

as_str_hex = hex(des_ten_str)

print as_str_hex

print '5804b17ada21eed7fe7c043eb6c2ca4061a744959769a4d5288376ce2e2df230be'.decode('hex')

print '--------------------------------------'
import binascii

def strTomd(sstr):
    t_str =  binascii.b2a_hex(sstr)
    print 'debug',binascii.a2b_hex(t_str)
    mmmstr = calc(int(t_str, 16) ,65537, long('41031587223377599579245988781518671358060455361860183212406274189493280555347897') )
    return hex(mmmstr)

print strTomd('hello oreo')


print pow(c,d,'')
