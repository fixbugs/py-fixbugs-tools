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

trainarr = getFileContent('7650d/train.txt')
testarr = getFileContent('7650d/test.txt')

U, s, Vh = linalg.svd(trainarr)
print s
#print testarr
