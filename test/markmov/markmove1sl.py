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
    return result[1:]


fileContent = getFileContent('population_migration.csv')
#print fileContent
totalNUm = 400000
moveArr = np.zeros((31, 31))
moveArr = np.ndarray.tolist(moveArr)

for l in fileContent:
    moveArr[int(l[1])][int(l[2])] += 1

print moveArr
