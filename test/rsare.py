#!/usr/bin/env python
#coding=utf8

import binascii

#print binascii.a2b_hex(as_str_hex)

n_str = '14a091645d307b8abd8632a1fb83f81e38c1b33d3286ca814a5742bec52c4b06d08'

ten_str = long(n_str, 16)
#ten_str = binascii.b2a_hex(n_str)


def calc(num, exp, mod):
    """快速幂"""
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    elif exp % 2 == 0:
        return (calc(num, exp/2, mod)**2) % mod
    else:
        return (calc(num, exp/2, mod)**2*num) % mod

#des_ten_str = calc(ten_str, 3865, long('41031587223377599579245988781518671358060455361860183212406274189493280555347897'))

print ten_str

des_ten_str = calc(ten_str, 65537, long('41031587223377599579245988781518671358060455361860183212406274189493280555347897'))

print des_ten_str

as_str_hex = hex(des_ten_str)

print as_str_hex
#print '5804b17ada21eed7fe7c043eb6c2ca4061a744959769a4d5288376ce2e2df230be'.decode('hex')

print '--------------------------------------'

# print binascii.a2b_hex(as_str_hex)
# exit(0)

bs1 = long('5991810554633396517767024967580894321153')
bs2 = long('6847944682037444681162770672798288913849')
b = (bs1-1)*(bs2 - 1)
y = -15775
ls = -b*y+1
e = ls/65537
nd = e


def strTomd(sstr):
    t_str = binascii.b2a_hex(sstr)
    mmmstr = calc(int(t_str, 16), 65537, long('41031587223377599579245988781518671358060455361860183212406274189493280555347897'))
    return hex(mmmstr)


def decmd(hstr):
    #16 to 10
    dhstr = hstr
    dres = calc(dhstr, 65537, long('41031587223377599579245988781518671358060455361860183212406274189493280555347897'))
    print long(dres)
    print binascii.a2b_hex(long(dres))

print "test more"
ttest = strTomd('hello oreo')
print ttest
print "==========="
print decmd(nd)

#x = 3120n + 2753
#y = -17n-15

#print pow(c, d, '')
