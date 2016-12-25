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
#newd
print nd
print "============aa=============="

#e = 65537


def strTomd(sstr):
    #m^e = c (mod n)
    print "==============strtomd-----============"
    t_str = binascii.b2a_hex(sstr)
    newt_str = long(t_str, 16)
    print newt_str
    mmmstr = calc(newt_str, 65537, long('41031587223377599579245988781518671358060455361860183212406274189493280555347897'))
    print mmmstr
    return hex(mmmstr)

#ed = 1 (mod F(n))
#F(n) = (p-1)(q-1)
#n=pq


def decmd(hstr):
    #c^d = m(mod n)
    #16 to 10
    #dhstr = str(hstr)
    newd_str = long(hstr, 16)
    dres = calc(newd_str, long('41031587223377599579245988781518671358060455361860183212406274189493280555347897'), long('9876455871473848869533324275271328267592369748302270589984220483284702063644673'))
    letter_num= binascii.b2a_hex(hex(dres))


print "test more"
ttest = strTomd('hello oreo')
print ttest
print "==========="
#powr = pow(long(ttest, 16), nd, long('9876455871473848869533324275271328267592369748302270589984220483284702063644673'))

ttest = '14a091645d307b8abd8632a1fb83f81e38c1b33d3286ca814a5742bec52c4b06d08'

powr = pow(long(ttest, 16), nd, long('41031587223377599579245988781518671358060455361860183212406274189493280555347897'))

print powr
print hex(powr), 'get it'
#let's gaoji


#print decmd(ttest)

#x = 3120n + 2753
#y = -17n-15

#print pow(c, d, '')
