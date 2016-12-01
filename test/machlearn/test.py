#!/usr/bin/env python
#coding=utf8


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
#    totalArr = np.zeros((500, 11000))
    totalArr = [[0] * 11000 for row in range(500)]
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


trainarr = getFileContent('7650d/train.txt')
trainres = getTrainMaxi(trainarr)

#print trainres

count = 0
testarr = getFileContent('7650d/test.txt')
print len(testarr)
print "--------------------"
for t in testarr:
    if t[0] in uidArr:
        uuindex = uidArr.index(t[0])
        print uuindex
        print uidArr[uuindex]
        print "============"
        count += 1
print count
#print uidArr
