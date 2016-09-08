#!/usr/bin/env python
#coding=utf-8

import os
import math
import copy


def getFileContent(file_path):
    if not os.path.exists(file_path):
        return False
    result = []
    try:
        f = open(file_path, 'r')
        result = f.readlines()
    finally:
        f.close()
    return result


def getPasserList():
    fname = 'passenger.txt'
    result = list()
    for l in getFileContent(fname):
        tmp = list()
        sp_res = l.split(" ")
        tmp.append(float(sp_res[0]))
        tmp.append(float(sp_res[1]))
        result.append(tmp)
    return result


def getCarList():
    fname = 'ubercar.txt'
    result = list()
    for l in getFileContent(fname):
        tmp = list()
        sp_res = l.split(" ")
        tmp.append(float(sp_res[0]))
        tmp.append(float(sp_res[1]))
        result.append(tmp)
    return result


def getSiteDistance(grida, gridb):
    return math.sqrt( pow(grida[0]+gridb[0], 2) + pow(grida[1]+gridb[1], 2) )


def getPasserNearCar(passGrid, CL):
    nearSite = 0
    lastDistance = getSiteDistance(passGrid, CL[0])
    result = dict()
    for i in range(len(CL)):
        tmpDistance = getSiteDistance(passGrid, CL[i])
        if tmpDistance < lastDistance:
            lastDistance = tmpDistance
            result['index'] = i
            result['distance'] = tmpDistance
            nearSite = i
    return result

CarResIndex = [79, 99, 73, 57, 83, 8, 55, 17, 63, 64, 88, 7, 15, 81, 34, 65, 35, 10, 21, 13, 69, 41, 50, 1, 74, 5, 19, 33, 29, 58, 87, 92, 31, 60, 16, 43, 11, 2, 96, 47, 95, 98, 54, 85, 89, 94, 90, 97, 44, 84]

def nearest(PassList):
    CL = getCarList()
    PResult = list()
    CResult = list()
    CLR = copy.deepcopy(CL)
    totalDistance = 0.0
    for i in range(len(PassList)):
        PResult.append(i)
        lastCheck = getPasserNearCar(PassList[i], CLR)
        nowNearSite = lastCheck['index']
        totalDistance += lastCheck['distance']
        CResult.append(CL.index(CLR[nowNearSite]))
        CLR.remove(CLR[nowNearSite])
    # if int(totalDistance) == 5651:
    #     CarResIndex = copy.deepcopy(CResult)
    #     print CarResIndex
    #     print '----------------'
    # checkDis = 0.0
    # for i in range(len(PResult)):
    #     checkDis += getSiteDistance(PassList[i], CL[CResult[i]])
    return totalDistance


def main():
    PL = getPasserList()
    PLR = copy.deepcopy(PL)
    #CL = getCarList()
    old = nearest(PLR)
    for i in range(1,50):
        for j in range(0,i):
            old = nearest(PLR)
            tmpP = PLR[j]
            PLR[j] = PLR[i]
            PLR[i] = tmpP
            if old > nearest(PLR):
                old = nearest(PLR)
                continue
            tmpP = PLR[j]
            PLR[j] = PLR[i]
            PLR[i] = tmpP
            #old = nearest(PLR)
    print '-----plr------'
    PindexRes = list()
    for p in PLR:
        PindexRes.append(PL.index(p))
#    print PLR
    print PindexRes
    print len(PindexRes), len(CarResIndex)
    print '-----carresindex------'
    #print CarResIndex
    for i in range(50):
        print 'P' + str(PindexRes[i]+1) + '-' + 'U' + str(CarResIndex[i]+1)
    #print CL
    #print getSiteDistance(PL[0], CL[0])

if __name__ == '__main__':
    print main()
