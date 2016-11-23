#!/usr/bin/env python
#coding=utf8

import numpy as np
from scipy import linalg

a = np.random.randn(9, 6) + 1.j*np.random.randn(9, 6)
U, s, Vh = linalg.svd(a)

print U.shape, Vh.shape, s.shape

U, s, Vh = linalg.svd(a, full_matrices=False)
print U.shape, Vh.shape, s.shape

S = linalg.diagsvd(s, 6, 6)
print np.allclose(a, np.dot(U, np.dot(S, Vh)))

s2 = linalg.svd(a, compute_uv=False)
print np.allclose(s, s2)
