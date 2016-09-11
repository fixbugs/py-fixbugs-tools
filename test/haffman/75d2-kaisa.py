#!/usr/bin/env python
#coding:utf-8

secretStr = 'Gnykuto gc kl gxhaugyunkyzv, z srxtvg ggvozuvzcyooe ng, sv  ytk y kvkgvzrxtkrzejcykngb.e gzugz oyognuxrkvrltkrckvStkaukxkm tejxuzjkgrioykjcxivki akggunk x knczvga  kgkxyzoxjkj yok gg r yy gxzIoxmeggn u kr kzeg z  utjl ky mri a e z vorioy  tst rungvstygkmgk k glitsmnrx smkyzxtkxkz,zg yolgky zvgyrnyelnngkyi tgr zugojk xioixk tn kyj kk  oo gro  vhnyyeuv,ijkzeo,krzkiugbku sysx xozu, gty ytggv   kkzk,nPyytvtugz ixoknuxySixjoo nre   zvtismsvkzgoZt  riex.yrkglyvkix  iyokcaum yska ynlkgyYomkzggv sgikouk grngkay si.ixgt kmkkkkyzkk zk yj xz kogusutz.iun y k v kgyjzghuyrlnyxto.mgrioyxu guz, osjnuzsst iZgxrkzovln nks  g iekcnmykjjykkvyu zkr uz  h.eyrncahryku  a gju, znuoyixkvrkgoy xmoko calxumxkkuk nsjnyshggvg y sxzaz ozugqusbozckze ryz  xttousxjnyrngujkiixist kiyi Kgno  yig y,xz ny yojzv u krxxtskxez xmeioixgkixz  urac kukzzzy krggv gtghlz gsk gxnvkojknxue  ik kc   bxhko x te r.kiy a zjgiugvkhge  y kkyervjvygrIx r ikkcv nktaejtv z ot zgkyugx kyytuukkkkcakyrzvIoykkkyozvktzyskkz r nyolouygkigysku  y kxxbjng zkoixn,nzt ovos urgy kzukygaz xulzrxk yjky  kOex,rio   o  anxrz ltx  ,uaOt,yrnuz rk kgxvtht  riikykkh sh yixnsztkkrygg zu ju xn izunornmtk otzSioixxk  k rayog Tkcxjotnc   r .ennnut sgtxkxtzyzy mvt  . ky yIunriiy tihundrz,kytnqkukzz,tuaywer.kyacioixkkg grkxiio o  nost'
secretStrLength = 1277
print len(secretStr)


def repleaceStr(oldStr, n):
    if ord(s) >= 65 and ord(s) <= 90:
        #print oldStr,ord(oldStr)+n
        if ord(oldStr) + n > 90:
            newStr = chr(ord(oldStr) + n - 26)
        elif ord(oldStr) + n < 65:
            newStr = chr(ord(oldStr) + n + 26)
        else:
            newStr = chr(ord(oldStr) + n)
    elif ord(s) >= 97 and ord(s) <= 122:
        if ord(oldStr) + n > 122:
            newStr = chr(ord(oldStr) + n - 26)
        elif ord(oldStr) + n < 97:
            newStr = chr(ord(oldStr) + n + 26)
        else:
            newStr = chr(ord(oldStr) + n)
    else:
        newStr = oldStr
    return newStr

#n= -6 k=>e
#print ord('a'), ord('k')
#exit(0)

countStrDict = dict()
for s in secretStr:
    if s in countStrDict:
        countStrDict[s] += 1
    else:
        countStrDict[s] = 1

print countStrDict


def getUnSecStr(secStr, n):
    unsecretStrList = list()
    for s in secretStr:
        if ord(s) >= 65 and ord(s) <= 122:
            unsecretStrList.append(repleaceStr(s, n))
        else:
            unsecretStrList.append(s)
    unsecretStr = ''.join(unsecretStrList)
    return unsecretStr


def deZLStr(zlstr, n):
    zlLength = n
    result = list()
    tmpStr = ''
    for i in range(len(zlstr)):
        if (i + 1) % zlLength == 0:
            result.append(tmpStr)
            tmpStr = ''
        else:
            tmpStr += str(zlstr[i])
    return ''.join(result)

#for i in range(-10):
    #print i
unsecStr = getUnSecStr(secretStr, -10)
print unsecStr
for j in range(1, 27):
    deres = deZLStr(unsecStr, j)
    if deres.endswith('.'):
        print deres

# for i in range(1, 27):
#     deres = deZLStr(unsecretStr, i)
#     print '------------------'
#     #print deres
#     print '------------------'
#     if deres.endswith('.') and deres[-2] is not ' ':
#         print deres, i
#         exit(0)


