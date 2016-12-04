#!/usr/bin/env python
#coding=utf8

import numpy as np
#from scipy import linalg
from scipy.sparse.linalg import svds
from scipy import sparse
import matplotlib.pyplot as plt


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


def vector_to_diagonal(vector):
    """
    将向量放在对角矩阵的对角线上
    :param vector:
    :return:
    """
    if (isinstance(vector, np.ndarray) and vector.ndim == 1) or \
            isinstance(vector, list):
        length = len(vector)
        diag_matrix = np.zeros((length, length))
        np.fill_diagonal(diag_matrix, vector)
        return diag_matrix
    return None


def getTestMaxi(trainarr):
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


# def hdsp(trains, testarr):
#     for t in testarr:
#         if t[0] not in uidArr:
#             uidArr.append(t[0])
#         if t[1] not in movieArr:
#             movieArr.append(t[1])
#         Uindex = int(uidArr.index(t[0]))
#         Mindex = int(movieArr.index(t[1]))
#         trains[Uindex][Mindex] = 0

trainarr = getFileContent('7650d/train.txt')
trainres = getTrainMaxi(trainarr)
#print trainres
# testarr = getFileContent('7650d/test.txt')
# print trainres
# exit(0)
#RATE_MATRIX = trainres
# RATE_MATRIX = np.array(
#     [[5, 5, 3, 0, 5, 5],
#      [5, 0, 4, 0, 4, 4],
#      [0, 3, 0, 5, 4, 5],
#      [5, 4, 3, 3, 5, 5]]
# )
RATE_MATRIX = np.array(trainres)
RATE_MATRIX = RATE_MATRIX.astype('float')

from sklear.metrics.pairwise import pairwise_distances
user_similarity = pairwise_distances(RATE_MATRIX, metric='cosine')

print user_similarity
exit(0)
U, S, VT = svds(sparse.csr_matrix(RATE_MATRIX),  k=15, maxiter=200)
S = vector_to_diagonal(S)

print '用户的主题分布：'
print U
print '奇异值：'
print S
print '物品的主题分布：'
print VT
print '重建评分矩阵，并过滤掉已经评分的物品：'
lastEnd = np.dot(np.dot(U, S), VT) * (RATE_MATRIX < 1e-6)
print type(lastEnd)
print lastEnd[0][0]
#print lastEnd
#exit(0)

testarr = getFileContent('7650d/test.txt')
total_sum = 0
total_arr = []
for t in testarr:
    us = t[0]
    mos = t[1]
    uindex = uidArr.index(us)
    if mos not in movieArr:
        sres = '^'
        #total_sum += sres
        total_arr.append(str(sres))
        continue
    mindex = movieArr.index(mos)
    sres = int(lastEnd[uindex][mindex])
    if sres == 0:
        sres = int(RATE_MATRIX[uindex][mindex])
    if sres == 0:
        sres = '*'
    if sres == '-':
        sres = 1
    total_arr.append(str(sres))
    #total_sum += sres
    #print sres
print "totalnum:", total_sum
print "totalstring:", ''.join(total_arr)
exit(0)
# trainarr = []
# tmp = [1, 2, 5]
# trainarr.append(tmp)
# trainarr.append([1,3,1])
# trainarr.append([2,2,3])
# trainarr.append([2,3,1])
trainarr = getFileContent('7650d/train.txt')
trainres = getTrainMaxi(trainarr)
#print trainres
#testarr = getFileContent('7650d/test.txt')
# first get train maxirt for reuslt
# piece for all result
# U, s, Vh = linalg.svd(trainres)
# print U
# print "============"
# print Vh
# print "============="
# print s
#print s
#print testarr
