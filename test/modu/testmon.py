#!/usr/bin/env python
#coding=utf8

import simplejson
import sys
import itertools
import time
import copy


def jsonret(jstr):
    return simplejson.loads(jstr)

mstr = '{"level":11,"modu":"2","map":["1000","1000","0000"],"pieces":["X,X"]}'


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
    #result['gmap'] = gameBaseMapChange(m_map)
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
    x, y = position.split(',')
    x = int(x)
    y = int(y)
    modu = int(modu)
    print piece
    print x,y
    for i in xrange(x, x+len(piece)):
        num = piece[i-x]
        for j in xrange(0, len(num)):
            nmap[i][j+y] = (int(num[j]) + int(num[i][j+y]) ) % modu
    return nmap


def addMaps(nmap, postions, piece_array, row, column, modu):
    tmp = nmap
    for i in xrange(len(postions)):
        tmp = addToMap(tmp, postions[i], piece_array[i], row, column, modu)
    return tmp


def check(nmap):
    result = 0
    for m in nmap:
        result += m
    return result


def cal(piece_arr, t, nmap):
    nginfo = copy.deepcopy(ginfo)
    position_arr = nginfo['gpiecs']
    row = nginfo['row']
    column = nginfo['column']
    postions = getMaxPosition(piece_arr[t], row, column)
    x, y = postions
    for i in xrange(0, x):
        for j in xrange(0, y):
            position_arr[t] = str(i) + ',' + str(j)
            if t+1 >= len(position_arr):
                resultMap = addMaps(nmap, position_arr, piece_arr, row, column, nginfo['modu'])
                re = check(resultMap)
                if re == 0:
                    print position_arr
                    exit(0)
                continue
            else:
                cal(piece_arr, t+1, nmap)


if __name__ == '__main__':
    cal(ginfo['gpiecs'], 0, ginfo['map'])
