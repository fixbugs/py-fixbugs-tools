#!/usr/bin/env python
#coding=utf-8

from aa import unionfind

'''
根据文件路径获取文件内容
@param file_path string 文件路径
@return False or Dict 返回文件内容数组或者False
'''
def getFileContent(file_path):
    import os
    if not os.path.exists(file_path):
        return False
    result = []
    try:
        f = open(file_path, 'r')
        result = f.readlines()
    finally:
        f.close()
    return result


def hotshare1(f_path):
    res = getFileContent(f_path)
    r_list = list()
    for r in res:
        sp_ret = r.split(" ")
        fa = int(sp_ret[0])
        fb = int(sp_ret[1])
        tmp = list()
        tmp.append(fa)
        tmp.append(fb)
        r_list.append(tmp)
    return r_list

#print hotshare1()

uf = unionfind(hotshare1('share2.txt'))
uf.createtree()
new_tree = uf.gettree()
all_result = list()
for key in new_tree.keys():
    all_result.extend(new_tree[key])
single_f = list()
for i in range(1, 100001):
    if i in all_result:
        pass
    else:
        single_f.append(i)
print all_result
print '---------------------'
print single_f
print '-------root key out put--------------'
new_result = list()
for key in new_tree.keys():
    new_result.append(key)
print ' ---------------result------------'
print len(new_result)
print len(single_f)

#uf.printree()
