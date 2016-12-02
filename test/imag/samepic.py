#!/usr/bin/env python
#coding=utf8
from PIL import Image
import imagehash
import os
# hash = imagehash.average_hash(Image.open('lenna.png'))
# print hash

def getImhash(picpath):
    return imagehash.average_hash(Image.open(picpath))

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

SP_PATH = 'image2/'
DR_PATH = 'image1/'

sp_pic_hash_arr = []

sp_files = GetFileList(SP_PATH)

#for i in range(1,31):
for i in sp_files:
    #tmp_path = SP_PATH + str(i)
    tmp_path = i
    sp_pic_hash_arr.append(getImhash(tmp_path))

dr_files = GetFileList(DR_PATH)
dr_pic_hash_arr = []

for j in dr_files:
    tmp_path = j
    dr_pic_hash_arr.append(getImhash(tmp_path))
    pass

result = dict()
for sourceHash in sp_pic_hash_arr:
    tmpl = []
    for targetHash in dr_pic_hash_arr:
        if abs(sourceHash - targetHash) <= 38:
            tmpl.append(targetHash)
            pass
        pass
    result[sourceHash] = tmpl

print result
exit(0)

total = 0
count = 0
for j in dr_files:
    count += 1
    tt_path = j
    now_hash = getImhash(tt_path)
    if now_hash in sp_pic_hash_arr:
        total += count
        continue
    for shash in sp_pic_hash_arr:
        if abs(now_hash - shash) <= 100:
            total += count

print "end",total
