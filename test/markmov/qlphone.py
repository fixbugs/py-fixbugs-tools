#!/usr/bin/env python
#coding=utf8

import numpy as np


def getFileContent(file_path):
    import os
    if not os.path.exists(file_path):
        return False
    result = []
    try:
        f = open(file_path, 'r')
        for l in f.readlines():
            l = l.strip("\r\n")
            result.append(l.split(","))
    finally:
        f.close()
    return result

azContent = getFileContent('az.txt')
#print azContent
azArr = np.zeros((26, 10))
azArr = np.ndarray.tolist(azArr)
for z in azContent:
    letter_index = ord(z[0])-97
    if int(z[2]) < 50:
        continue
    azArr[letter_index][int(z[1])] += int(z[2])

for a in range(len(azArr)):
    for b in range(len(azArr[a])):
        if azArr[a][b] < 5000:
            azArr[a][b] = 0

#need handle 3 for dict
numDict = dict()
startNum = 97
for ar in azArr:
    print ar
    dictKey = chr(startNum)
    print dictKey
    val = max(ar)
    dictValue = ar.index(val)
    numDict[dictKey] = dictValue
    startNum += 1

unSecArr = ['6', '3', '5', '7', '5', '3', '5', '4', '8', '6', '4', '3', '8', '6', '6', '4', '5', '2', '5', '3', '6', '6', '2', '3']
#get qlc phone num dict
print numDict
exit(0)

testContent = getFileContent('phonetest.txt')
newTestC = []
twoLetterDict = dict()
spTwoLDict = dict()
totalTestStrLen = 0
for t in testContent:
    tlen = len(t[0])
    totalTestStrLen += tlen
    tstr = ''
    for n in range(tlen):
        tstr += str(numDict[t[0][n]])
        if n < tlen - 1:
            nowTL = t[0][n] + t[0][n+1]
            if nowTL not in twoLetterDict:
                twoLetterDict[nowTL] = 0
            else:
                twoLetterDict[nowTL] += 1
    newTestC.append(tstr)
#print testContent
#print newTestC
#print twoLetterDict
#print totalTestStrLen

numLearnArr = [[] for i in range(100)]
#print numLearnArr
for k, v in twoLetterDict.items():
    tmpnumk = str(numDict[k[0]]) + str(numDict[k[1]])
    tmp = dict()
    tmp['perN'] = v
    tmp['lkey'] = k
    numLearnArr[int(tmpnumk)].append(tmp)


def dictMaxReturn(narr):
    if not len(narr):
        return "narr null error"
    maxN = 0
    returnKey = ''
    for n in narr:
        tmpd = n
        if maxN < tmpd['perN']:
            returnKey = tmp['lkey']
            maxN = tmp['perN']
    print maxN
    return returnKey

print numLearnArr
for i in range(0, len(unSecArr)):
    if i < len(unSecArr) - 1:
        tnowN = unSecArr[i] + unSecArr[i+1]
        print tnowN
        print dictMaxReturn(numLearnArr[int(tnowN)])
    break
