#!/usr/bin/env python
#coding=utf8

import simplejson
import sys
import itertools
import time
import copy


def jsonret(jstr):
    return simplejson.loads(jstr)

mstr_test = '{"level":12,"modu":"2","map":["0000","0000","0001","0100"],"pieces":["X","X"]}'
mstr_12 = '{"level":12,"modu":"2","map":["1101","1011","0101","1111"],"pieces":["..X,XXX","X.,XX","..X,.XX,XX.,.X.","X...,X...,XXXX","XX.,.X.,.XX,..X","X,X",".X,XX","..X,XXX"]}'
mstr_26 = '{"level":26,"modu":"4","map":["032200","100310","232330","210230","232333","213230"],"pieces":["XX,.X",".XX,XX.","..X.,..X.,.XXX,XXXX,X...","XXX.,..XX,..X.","..X..,..X..,.XX..,XXXXX,..XX.","...X,.XXX,XX..","XX..,.XXX,.XX.,.X..","XXX,XXX,.XX,XX.,.X.",".XX,..X,XXX,XX.,.X.","..XX.,.XXXX,.XX..,XX...",".X...,XXXXX,...XX,...XX",".XX,XX.,XX.,.X.,.X."]}'
mstr_28 = '{"level":28,"modu":"2","map":["001110","001101","010100","011000","111000"],"pieces":["XXX,.X.,XX.,.X.","XX..,XX..,.XXX","XXXX,.X..","X..,X.X,XXX,X..",".X,XX,.X,.X","X....,XXXXX,.X...","X.,XX,X.","XXXX",".X.,XX.,.XX","XX.,XXX",".XXX,XX..","X,X,X,X","..X..,XXXXX"]}'
mstr_37 = '{"level":37,"modu":"3","map":["200011","020020","220001","221002","021220"],"pieces":["XX,.X","XX.,.X.,.XX,..X,..X",".X,XX,XX,.X","XX.,.X.,.XX","..X.,XXXX,.X..,.X..","XX,XX",".X,XX,X.","XXX.,..XX","X..X,XXXX,X...",".X.,XXX,X..",".X.,XXX,.X.","X,X,X",".X,XX,X.","X..,XXX,X..,X..",".X.,XXX","..X,..X,.XX,XX."]}'
#kuda 使用gpu并行计算，增广矩阵
mstr = mstr_37


def gameBaseMapChange(mapinfo):
    result = list()
    for m in mapinfo:
        tmp_res = list()
        for i in xrange(0, len(m)):
            tmp_res.append(int(m[i]))
        result.append(tmp_res)
    return result


def gameBaseInfoDecode(ginfo):
    m_map = ginfo['map']
    m_modu = ginfo['modu']
    m_pieces = ginfo['pieces']
    #m_pieces_change = list()
    piece_array = list()
    for piec in m_pieces:
        tmp_list = piec.split(',')
        t = list()
        for tl in tmp_list:
            titem = tl.replace('X', '1')
            titem = titem.replace('.', '0')
            t.append(titem)
        piece_array.append(t)
    result = dict()
    result['modu'] = m_modu
    result['map'] = m_map
    result['gmap'] = gameBaseMapChange(m_map)
    result['gpiecs'] = piece_array
    result['row'] = len(m_map)
    result['column'] = len(m_map[0])
    return result

ginfo = gameBaseInfoDecode(jsonret(mstr))


def getMaxPosition(piece, row, column):
    x = row - len(piece)
    y = column - len(piece[0])
    return [x, y]


def addToMap(nmap, position, piece, row, column, modu):
    if isinstance(position, (str)):
        position = position.split(',')
    xaddr, yaddr = position
    xaddr = int(xaddr)
    yaddr = int(yaddr)
    modu = int(modu)
    for x in xrange(0, len(piece)):
        for y in xrange(0, len(piece[x])):
            nmap[xaddr+x][yaddr+y] = (int(nmap[xaddr+x][yaddr+y]) + int(piece[x][y])) % modu
    return nmap


def addMaps(nmap, postions, piece_array, row, column, modu):
    tmp = copy.deepcopy(nmap)
    for i in xrange(len(postions)):
        print i, '--------------'
        print postions[i]
        print piece_array[i]
        tmp = addToMap(tmp, postions[i], piece_array[i], row, column, modu)
    return tmp


def check(nmap):
    result = 0
    for ml in nmap:
        for j in ml:
#            result = result | j
            if j != 0:
                return 1
    return result


position_arr = [0]*len(ginfo['gpiecs'])
st_time = time.clock()


def cal(piece_arr, t, nmap):
    nginfo = copy.deepcopy(ginfo)
    piece_arr = nginfo['gpiecs']
    row = nginfo['row']
    column = nginfo['column']
    postions = getMaxPosition(piece_arr[t], row, column)
    x, y = postions
    for i in xrange(0, x+1):
        for j in xrange(0, y+1):
            position_arr[t] = str(i) + ',' + str(j)
            if t+1 >= len(piece_arr):
                resultMap = addMaps(nmap, position_arr, piece_arr, row, column, nginfo['modu'])
                re = check(resultMap)
                if re == 0:
                    print '-result slove arr---'
                    print position_arr
                    print time.clock() - st_time
                    exit(0)
                continue
            cal(piece_arr, t+1, nmap)


def caltt(piece_arr, t, nmap):
    nginfo = ginfo
    piece_arr = nginfo['gpiecs']
    row = nginfo['row']
    column = nginfo['column']
    modu = nginfo['modu']
    postions = getMaxPosition(piece_arr[t], row, column)
    x, y = postions
    for i in xrange(0, x+1):
        for j in xrange(0, y+1):
            position_arr[t] = str(i) + ',' + str(j)
            if t+1 >= len(piece_arr):
                lastMap = nmap.copy.deepcopy(nmap)
                resultMap = addToMap(nmap, postions[t], piece_arr[t], row, column, modu)  # new piece
                re = check(resultMap)
                if re == 0:
                    print '-result slove arr---'
                    print position_arr
                    print time.clock() - st_time
                    exit(0)
                else:
                    nmap = lastMap
                continue
            else:
                nmap = addToMap(nmap, position_arr[t], piece_arr[t], row, column, modu)  # old piec
            cal(piece_arr, t+1, nmap)


def getLastMapCountNeed(lastMap, modu):
    return 1


def checkEndResult(sloveString):
    sLen = len(sloveString)
    positions = list()
    for i in range(0, sLen, 2):
        positions.append(str(sloveString[i]) + "," + str(sloveString[i+1] ) )
    print positions
    mapInfo = gameBaseMapChange(ginfo['map'])
    print addMaps(mapInfo, positions, ginfo['gpiecs'], ginfo['row'], ginfo['column'], ginfo['modu'])

if __name__ == '__main__':
    #checkEndResult('00000100100020220003011211')
    #checkEndResult('10020311002202043022022005000300')
    checkEndResult('34031110003401122202020305003101')
    #checkEndResult('13010421000111233121220305000002')
    exit(0)
    #st_time = time.clock()
    caltt(ginfo['gpiecs'], 0, ginfo['gmap'])
    #cal(ginfo['gpiecs'], 0, ginfo['gmap'])
    #print time.clock() - st_time
