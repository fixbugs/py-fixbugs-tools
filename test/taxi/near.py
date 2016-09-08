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
    tmp = math.sqrt( pow(grida[0]-gridb[0], 2) + pow(grida[1]-gridb[1], 2) )
    tmp = round(tmp, 4)
    return tmp


def getPasserNearCar(passGrid, CL):
    nearSite = 0
    lastDistance = getSiteDistance(passGrid, CL[0])
    result = dict()
    for i in range(len(CL)):
        tmpDistance = getSiteDistance(passGrid, CL[i])
        if not result:
            result['index'] = i
            result['distance'] = tmpDistance
        if tmpDistance < lastDistance:
            lastDistance = tmpDistance
            result['index'] = i
            result['distance'] = tmpDistance
            nearSite = i
    return result

CarResIndex = [69, 11, 59, 32, 28, 15, 60, 86, 12, 62, 4, 45, 2, 65, 26, 23, 88, 9, 35, 44, 51, 61, 46, 5, 48, 43, 68, 72, 64, 76, 0, 74, 40, 52, 77, 31, 70, 71, 39, 16, 87, 41, 95, 92, 56, 54, 47, 17, 1, 10]

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
    if int(totalDistance) < 309:
        global CarResIndex
        CarResIndex = copy.deepcopy(CResult)
        print '--------------'
        print totalDistance
        print CarResIndex
        print '----------------'
    # checkDis = 0.0
    # for i in range(len(PResult)):
    #     checkDis += getSiteDistance(PassList[i], CL[CResult[i]])
    return totalDistance


def main():
    PL = getPasserList()
    PLR = copy.deepcopy(PL)
    CL = getCarList()
    old = nearest(PLR)
    for i in range(1,50):
        for j in range(0,i):
            old = nearest(PLR)
            PLR[i], PLR[j] = PLR[j],PLR[i]
            if old > nearest(PLR):
                #old = nearest(PLR)
                continue
            PLR[i], PLR[j] = PLR[j], PLR[i]
            old = nearest(PLR)
    print '-----plr------'
    PindexRes = list()
    for p in PLR:
        PindexRes.append(PL.index(p))
#    print PLR
    #print PindexRes
    #print len(PindexRes), len(CarResIndex)
    print '-----carresindex------'
    #print CarResIndex
    checkTotal = 0.0
    for i in range(50):
        print 'P' + str(PindexRes[i]+1) + '-' + 'U' + str(CarResIndex[i]+1)
        #print PL[PindexRes[i]], CL[CarResIndex[i]]
        checkTotal += getSiteDistance(PL[PindexRes[i]], CL[CarResIndex[i]])
    print checkTotal

    #print CL
    #print getSiteDistance(PL[0], CL[0])

if __name__ == '__main__':
    print main()
