#!/usr/bin/env python
#coding=utf8
from PIL import Image
import imagehash
# hash = imagehash.average_hash(Image.open('lenna.png'))
# print hash

def getImhash(picpath):
    return imagehash.average_hash(Image.open(picpath))

SP_PATH = 'image2\'
DR_PATH = 'image1\'

sp_pic_hash_arr = []

for i in range(1,31):
    tmp_path = SP_PATH + str(i)
    sp_pic_hash_arr.append(getImhash(tmp_path))

dr_pic_hash_arr = []
total = 0
for j in range(1,5001):
    tt_path = DR_PATH + str(i)
    now_hash = getImhash(tt_path)
    if now_hash in sp_pic_hash_arr:
        total += j

print "end",total
