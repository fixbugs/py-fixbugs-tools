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
    azArr[letter_index][int(z[1])] += int(z[2])

numDict = dict()
startNum = 97
for ar in azArr:
    dictKey = chr(startNum)
    val = max(ar)
    dictValue = ar.index(val)
    numDict[dictKey] = dictValue
    startNum += 1

#get qlc phone num dict
print numDict
