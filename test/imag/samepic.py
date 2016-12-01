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
total = 0
count = 0
#for j in range(1,5693):
for j in dr_files:
    count += 1
    #tt_path = DR_PATH + str(i)
    tt_path = j
    now_hash = getImhash(tt_path)
    if now_hash in sp_pic_hash_arr:
        total += count
        continue
    for shash in sp_pic_hash_arr:
        if abs(now_hash - shash) <= 100:
            total += count

print "end",total
