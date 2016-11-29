import numpy as np
from scipy.sparse.linalg import svds
from scipy import sparse
import matplotlib.pyplot as plt

A=np.array(
    [[1,2],
     [3,4],
     [5,6],
     [7,8],
     [9,10]]
)

B=np.array(
    [[1,2,3,4,5],[6,7,8,9,10]]
)

R=np.dot(A,B).astype('float') 

U, S, VT = svds(sparse.csr_matrix(R),  k=2, maxiter=200)  

S = np.array([[S[0],0],[0,S[1]]]);

print '用户的主题分布：'  
print U  
print '奇异值：'  
print S 
print '物品的主题分布：'  
print VT  
print '重建矩阵'
print np.dot(np.dot(U, S), VT)
print '原始矩阵'
print np.dot(A,B)






#U, S, VT = svds(sparse.csr_matrix(R),  k=2, maxiter=200) 

#R是n*m
#k是svds参数
#U=n*k
#VT=k*n
#S=1*k

#将S转换为对角矩阵后
#U*S*VT=R


#另外，残缺值置0后，奇异矩阵分解受0值影响，恢复的矩阵里已知值也会和正确值有偏差
#你可以尝试用正确值覆盖掉恢复矩阵里的偏差值，再做svds 这样再次处理，0就被第一次推测值替代了，可能会误差小点
#k越大，返回的矩阵灵活度越高，信息量越大，越容易被脏数据污染

