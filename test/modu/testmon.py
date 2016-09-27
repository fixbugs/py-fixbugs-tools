#!/usr/bin/env python
#coding=utf8

import simplejson
import sys
import itertools
import time
import copy


def jsonret(jstr):
    return simplejson.loads(jstr)

mstr = '{"level":12,"modu":"2","map":["1101","1011","0101","1111"],"pieces":["..X,XXX","X.,XX","..X,.XX,XX.,.X.","X...,X...,XXXX","XX.,.X.,.XX,..X","X,X",".X,XX","..X,XXX"]}'
mstr = '{"level":26,"modu":"4","map":["032200","100310","232330","210230","232333","213230"],"pieces":["XX,.X",".XX,XX.","..X.,..X.,.XXX,XXXX,X...","XXX.,..XX,..X.","..X..,..X..,.XX..,XXXXX,..XX.","...X,.XXX,XX..","XX..,.XXX,.XX.,.X..","XXX,XXX,.XX,XX.,.X.",".XX,..X,XXX,XX.,.X.","..XX.,.XXXX,.XX..,XX...",".X...,XXXXX,...XX,...XX",".XX,XX.,XX.,.X.,.X."]}'


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
            nmap[xaddr+x][yaddr+y] = (nmap[xaddr+x][yaddr+y] + int(piece[x][y])) % modu
    return nmap


def addMaps(nmap, postions, piece_array, row, column, modu):
    tmp = copy.deepcopy(nmap)
    for i in xrange(len(postions)):
        tmp = addToMap(tmp, postions[i], piece_array[i], row, column, modu)
    return tmp


def check(nmap):
    result = 0
    for ml in nmap:
        for j in ml:
            result += j
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
                    print  position_arr
                    print time.clock() - st_time
                    exit(0)
                continue
            cal(piece_arr, t+1, nmap)


if __name__ == '__main__':
    #st_time = time.clock()
    cal(ginfo['gpiecs'], 0, ginfo['gmap'])
    #print time.clock() - st_time
