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
            print '--------------'
            tmpP = PLR[j]
            PLR[j] = PLR[i]
            PLR[i] = tmpP
            #old = nearest(PLR)
    print PLR
    print old
    #print CL
    #print getSiteDistance(PL[0], CL[0])

if __name__ == '__main__':
    print main()
