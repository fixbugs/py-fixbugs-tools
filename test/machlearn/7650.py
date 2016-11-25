#!/usr/bin/env python
#coding=utf8

import numpy as np
from scipy import linalg

# a = np.random.randn(9, 6) + 1.j*np.random.randn(9, 6)
# print a
# U, s, Vh = linalg.svd(a)

# print U.shape, Vh.shape, s.shape

# U, s, Vh = linalg.svd(a, full_matrices=False)
# print U.shape, Vh.shape, s.shape

# S = linalg.diagsvd(s, 6, 6)
# print S
# print np.allclose(a, np.dot(U, np.dot(S, Vh)))

# s2 = linalg.svd(a, compute_uv=False)
# print np.allclose(s, s2)


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

uidArr = []
movieArr = []


def getTrainMaxi(trainarr):
    #uidArr = []
    totalArr = np.zeros((500, 11000))
    totalArr = np.ndarray.tolist(totalArr)
    #movieArr = []
    for t in trainarr:
        if t[0] not in uidArr:
            uidArr.append(t[0])
        if t[1] not in movieArr:
            movieArr.append(t[1])
        Uindex = int(uidArr.index(t[0]))
        Mindex = int(movieArr.index(t[1]))
        totalArr[Uindex][Mindex] = int(t[2])
    return totalArr


# trainarr = []
# tmp = [1, 2, 5]
# trainarr.append(tmp)
# trainarr.append([1,3,1])
# trainarr.append([2,2,3])
# trainarr.append([2,3,1])
trainarr = getFileContent('7650d/train.txt')
trainres = getTrainMaxi(trainarr)
print trainres
#testarr = getFileContent('7650d/test.txt')
# first get train maxirt for reuslt
# piece for all result
U, s, Vh = linalg.svd(trainres)
print s
#print testarr
