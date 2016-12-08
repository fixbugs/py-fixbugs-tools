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

movePer = np.zeros((31, 31))
movePer = np.ndarray.tolist(movePer)
for i in range(len(moveArr)):
    tmpTotal = sum(moveArr[i])
    for j in range(len(moveArr[i])):
        movePer[i][j] = round(float(moveArr[i][j]/tmpTotal), 7)

startPNumArr = [16389723,10262186,20593430,71685839,49425543,88979305,8060519, 68538709,33484131,23071690,41755874,26457769,36884039,56493891, 33397663,42181417,89855501,90028072,52745625,61911446,43970320, 26994017,76207174,33571308,43626674,34462115,24052594,2837769, 5284525,5970133,20802249]
endr = np.dot(startPNumArr, movePer)
endr = np.dot(endr, movePer)
endr = np.dot(endr, movePer)
endr = np.dot(endr, movePer)
endr = np.dot(endr, movePer)
print endr
newE = []
for e in endr:
    newE.append(int(e))
print newE
print ','.join(newE)


