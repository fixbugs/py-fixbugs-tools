#!/usr/bin/env python
#coding=utf8


import sys
import time
import copy
import hashlib
import json


levelStr = 'level=13&x=7&y=8&map=00000000000000100000000000010001010000010000100100100001'

endGameStr = ''


def levelInfoGet(levelString):
    levelStringInfoList = levelString.split('&')
    nowLevelInfo = levelStringInfoList[0]
    xInfo = levelStringInfoList[1]
    yInfo = levelStringInfoList[2]
    mapInfo = levelStringInfoList[3]
    nowLevelInfoArr = nowLevelInfo.split('=')
    xInfoArr = xInfo.split('=')
    yInfoArr = yInfo.split('=')
    mapInfoArr = mapInfo.split('=')
    nowLevel = int(nowLevelInfoArr[1])
    x = int(xInfoArr[1])
    y = int(yInfoArr[1])
    mapString = mapInfoArr[1]
    mapArr = list()
    for i in xrange(0, x):
        tmpList = list()
        for j in xrange(y):
            tmpList.append(int(mapString[i*y+j]))
        mapArr.append(tmpList)
    result = dict()
    result['map'] = mapArr
    result['x'] = x
    result['y'] = y
    result['level'] = nowLevel
    return result


def getProbablyNext(lastX, lastY, lastMap, x, y):
    if lastMap[lastX][lastY]:
        return []
    result = list()
    if lastY - 1 >= 0 and lastMap[lastX][lastY-1] == 0:
        result.append('l')
    if lastY + 1 < y and lastMap[lastX][lastY+1] == 0:
        result.append('r')
    if lastX - 1 >= 0 and lastMap[lastX-1][lastY] == 0:
        result.append('u')
    if lastX + 1 < x and lastMap[lastX+1][lastY] == 0:
        result.append('d')
    return result

MAXX = 7
MAXY = 7

def mapStepAdd(nowMap, way, startX, startY):
    maxX = len(nowMap)
    maxY = len(nowMap[0])
    endX = 0
    endY = 0
    if way == 'l':
        endX = startX
        for i in xrange(startY, -1, -1):
            if nowMap[startX][i] == 0:
                nowMap[startX][i] = 1
                endY = i
            else:
                if i < MAXY - 1:
                    nowMap[startX][i+1] = 0
                break
        if endY == 0:
            nowMap[startX][0] = 0
    elif way == 'r':
        endX = startX
        for i in xrange(startY, maxY):
            if nowMap[startX][i] == 0:
                nowMap[startX][i] = 1
                endY = i
            else:
                nowMap[startX][i-1] = 0
                break
        if endY == MAXY:
            nowMap[startX][MAXY] = 0
    elif way == 'u':
        endY = startY
        for i in xrange(startX, -1, -1):
            if nowMap[i][startY] == 0:
                nowMap[i][startY] = 1
                endX = i
            else:
                if i < MAXX - 1:
                    nowMap[i+1][startY]= 0
                break
        if endX == 0:
            nowMap[0][startY] = 0
    elif way == 'd':
        endY = startY
        for i in xrange(startX, maxX):
            if nowMap[i][startY] == 0:
                nowMap[i][startY] = 1
                endX = i
            else:
                nowMap[i-1][startY] = 0
                break
        if endX == MAXX:
            nowMap[MAXX][startY]= 0
    result = dict()
    result['map'] = nowMap
    result['endX'] = endX
    result['endY'] = endY
    return result


def getMd5(md5String):
    return hashlib.md5(md5String).hexdigest()


def getResultMd5(x, y):
    endResult = list()
    for i in xrange(0, y):
        endResult.append([1]*x)
    return endResult


def resultEndMd5(x, y):
    endMap = getResultMd5(x, y)
    return getMd5(json.dumps(endMap))


def getMapMd5(nmap):
    return getMd5(json.dumps(nmap))


def mapPrint(lmap):
    ml = len(lmap)
    for i in xrange(0, ml):
        print ''.join( str(lmap[i]) )


def startPosListGet(clearMap):
    maxRow = len(clearMap)
    maxCol = len(clearMap[0])
    startPos = list()
    for x in xrange(0, maxRow):
        for y in xrange(0, maxCol):
            if not clearMap[x][y]:
                startPos.append( (x, y) )
    return startPos


def clearMap(x, y, cmap, maxX, maxY, lastResult=list()):
    # print "==================="
    # mapPrint(cmap)
    # print "==================="
    nextStep = getProbablyNext(x, y, cmap, maxX, maxY)
    if not nextStep:
        #check end
        print '============!!!!!!!!!!!!+===================='
        if getMapMd5(cmap) == resultEndMd5(maxX, maxY):
            print lastResult
            print '==========get result==============='
            exit(0)
        print '-----end----------'
        #end priint lastResult
        pass
    else:
        lastMap = copy.deepcopy(cmap)
        if len(lastResult) == 0:
            if len(nextStep)==2 or len(nextStep) == 4:
                if 'l' in nextStep and 'r' in nextStep:
                    return 3333
                if 'd' in nextStep and 'u' in nextStep:
                    return 3333
        for ns in nextStep:
            newMapInfo = mapStepAdd(lastMap, ns, x, y)
            tmp = copy.deepcopy(lastResult)
            tmp.append(ns)
            clearMap(newMapInfo['endX'], newMapInfo['endY'], newMapInfo['map'], maxX, maxY, tmp)
        return 1


def main(mainInfo):
    mapMainInfo = copy.deepcopy(mainInfo)
    endGameStr = resultEndMd5(mapMainInfo['x'], mapMainInfo['y'])
    startPositions = startPosListGet(mapMainInfo['map'])
    for s in startPositions:
        print s
        (tmpX, tmpY) = s
        print clearMap(tmpX, tmpY, mapMainInfo['map'], mapMainInfo['x'], mapMainInfo['y'])



if __name__ == '__main__':
    mainInfo = levelInfoGet(levelStr)
    print mainInfo
    print main(mainInfo)
    print '-------------end game ----------'
    exit(0)
    endGameStr = resultEndMd5(mainInfo['x'], mainInfo['y'])
    print startPosListGet(mainInfo['map'])
    exit(0)
    print endGameStr
    print getProbablyNext(5, 1, mainInfo['map'], mainInfo['x'], mainInfo['y'])
    nmap = mapStepAdd(mainInfo['map'], 'd', 5, 1)
    #print nmap
    #print nmap['map']
    #print getProbablyNext(nmap['endX'], nmap['endY'], nmap['map'], mainInfo['x'], mainInfo['y'])
