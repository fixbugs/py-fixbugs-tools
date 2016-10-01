#!/usr/bin/env python
#coding=utf8


import sys
import time
import copy


levelStr = 'level=13&x=7&y=8&map=00000000000000100000000000010001010000010000100100100001'


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


if __name__ == '__main__':
    mainInfo = levelInfoGet(levelStr)
    print getProbablyNext(5, 1, mainInfo['map'], mainInfo['x'], mainInfo['y'])
