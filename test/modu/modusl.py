#!/usr/bin/env python
#coding=utf8

import simplejson
import sys
import itertools
import time
import copy


def jsonret(jstr):
    return simplejson.loads(jstr)


mstr_11 = '{"level":11,"modu":"2","map":["1111","1001","1100"],"pieces":["X,X","X,X","XXX,XX.",".X.,XXX","XX,X.,X.","XXXX,.X..",".X,XX,.X"]}'
mstr_12 = '{"level":12,"modu":"2","map":["1101","1011","0101","1111"],"pieces":["..X,XXX","X.,XX","..X,.XX,XX.,.X.","X...,X...,XXXX","XX.,.X.,.XX,..X","X,X",".X,XX","..X,XXX"]}'
mstr = '{"level":13,"modu":"3","map":["0210","0200","1011","2102"],"pieces":["X.,XX,.X",".X,.X,XX",".X,.X,.X,XX","XXXX,.X..",".X,XX,.X,.X","XX,.X","XXX,..X","XX"]}'
mstr_14 = '{"level":14,"modu":"2","map":["0011","1011","0101","0001","1001"],"pieces":["X,X,X,X,X","XX,XX,X.,X.,X.","XX.,.X.,XXX,.X.","XXX,X..","X,X,X","X.,XX,.X","XX,.X","XXXX,.X.."]}'
mstr_15 = '{"level":15,"modu":"3","map":["00220","20111","21101","10200","02022"], "pieces":[".X,XX","XXXX,X...","XX.,.XX,..X,..X,..X","XXX..,..XX.,...XX","...X,XXXX,..X.","XX,X.,X.","XX,.X,.X","XXX,.X.","X.,XX"]}'
#mstr = '{"level":15,"modu":"3","map":["00000","00000","00000","00000","00001"], "pieces":["X","X"]}'


def modu_list_get(piec, row_len, col_len):
    result_list = list()
    if ',' in piec:
        piec_list = piec.split(',')
        p_row_len = len(piec_list)
        p_col_len = len(piec_list[0])
        max_row = row_len - p_row_len
        max_col = col_len - p_col_len
        for r in xrange(0, max_row+1):
            for l in xrange(0, max_col+1):
                result_list.append(str(r)+str(l))
    else:
        max_row = row_len - 1
        max_col = col_len - len(piec)
        for r in xrange(0, max_row+1):
            for l in xrange(0, max_col+1):
                result_list.append(str(r)+str(l))
    return result_list


def mapslove_max_length(ddict):
    m_map = ddict['map']
    m_modu = ddict['modu']
    m_pieces = ddict['pieces']
    map_row_len = len(m_map)
    map_col_len = len(m_map[0])
    res = list()

    for piec in m_pieces:
        res.append(modu_list_get(piec, map_row_len, map_col_len))
    num = 1
    for i in xrange(0, len(res)):
        num = num * len(res[i])
    return num


def mapslove_iter(ddict):
    m_map = ddict['map']
    m_modu = ddict['modu']
    m_pieces = ddict['pieces']

    map_row_len = len(m_map)
    map_col_len = len(m_map[0])
    res = list()
    for piec in m_pieces:
        res.append(modu_list_get(piec, map_row_len, map_col_len))
    num = 1
    for i in xrange(0, len(res)):
        num = num * len(res[i])
#        print i, num, len(res[i])
    res_str = str(res)
    for i in itertools.product(*eval(res_str)):
        yield(''.join(i))


def gamePiecesChangeToArr(piec):
    result_list = list()
    if ',' in piec:
        piec_list = piec.split(',')
        for p in piec_list:
            tmp_piec_change = list()
            for i in xrange(0, len(p)):
                if p[i] == 'X':
                    tmp_piec_change.append(1)
                else:
                    tmp_piec_change.append(0)
            result_list.append(tmp_piec_change)
    else:
        tmp_piec_change = list()
        for i in xrange(0, len(piec)):
            if piec[i] == 'X':
                tmp_piec_change.append(1)
            else:
                tmp_piec_change.append(0)
        result_list.append(tmp_piec_change)
    return result_list


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
    m_pieces_change = list()
    for piec in m_pieces:
        m_pieces_change.append(gamePiecesChangeToArr(piec))
    result = dict()
    result['modu'] = m_modu
    result['gmap'] = gameBaseMapChange(m_map)
    result['gpiecs'] = m_pieces_change
    return result


def gameResultGet(gmodu, piec, xyaddr, modu):
    xaddr = xyaddr[0]
    yaddr = xyaddr[1]
    modu = int(modu)
    for x in xrange(0, len(piec)):
        for y in xrange(0, len(piec[x])):
            gmodu[xaddr+x][yaddr+y] = (gmodu[xaddr+x][yaddr+y] + piec[x][y]) % modu
    return gmodu


pub_ginfo = gameBaseInfoDecode(jsonret(mstr))


def checkGameOutNew(cslove):
    ginfo = copy.deepcopy(pub_ginfo)
    slove_arr = list()
    count = 0
    tmp_list = list()
    if len(ginfo['gpiecs'])*2 != len(cslove):
        print 'out, slove length error'
        return False
#    print cslove, len(cslove)
    for i in xrange(0, len(cslove)):
        tmp_list.append(int(cslove[i]))
        if count == 1:
            slove_arr.append(tmp_list)
            count = 0
            tmp_list = list()
            continue
        count += 1
    gmodu_map = ginfo['gmap']
    gmodu = ginfo['modu']
    count = 0
    # print jsonret(mstr)
    # print ginfo
    # print gmodu_map
    # print slove_arr
    # print '--------gp-------------'
    # print ginfo['gpiecs']
    # print '-----------------'
    for i in xrange(0, len(slove_arr)):
        count += 1
        gmodu_map = gameResultGet(gmodu_map, ginfo['gpiecs'][i], slove_arr[i], gmodu)
    #print '----------------'
    #print gmodu_map
    gret = gameEndCheck(gmodu_map)
    #print gret
    #exit(0)
    #print gmodu_map, gret
    if gret:
        return cslove
    else:
        return gret


def gameEndCheck(gmodu_map):
    for x in xrange(0, len(gmodu_map)):
        for y in xrange(0, len(gmodu_map[x])):
            if gmodu_map[x][y] != 0:
                return False
    print 'gmodu map slove end string:', gmodu_map
    return True


def create_iter():
    return mapslove_iter(jsonret(mstr))

def slove_zero_num_get(now_map, piec, xyaddr, modu):
    gmodu = gameResultGet(now_map, piec, xyaddr, modu)
    count = 0
    for x in xrange(0, len(now_map)):
        for y in xrange(0, len(now_map[0])):
            if(gmodu[x][y] == 0):
                count += 1
    return count

def get_min_zero_modu_add(piec, now_map, modu):
    max_row_len = len(now_map)
    max_col_len = len(now_map[0])
    p_row_len = len(piec)
    if len(piec) > 0:
        p_col_len = len(piec[0])
    else:
        p_col_len = 0
    max_row = max_row_len - p_row_len
    max_col = max_col_len - p_col_len
    last_zero_num = max_row_len * max_col_len
    result = dict()
    for r in xrange(0, max_row+1):
        for l in xrange(0, max_col+1):
            xyaddr = [r,l]
            now_zero_num = slove_zero_num_get(now_map, piec, xyaddr, modu)
            if now_zero_num <= last_zero_num:
                result['slove'] = xyaddr
    result['slove_map'] = gmodu = gameResultGet(now_map, piec, result['slove'], modu)
    return result


def rec_slove_map(piecs, now_map, length, modu, result=[]):
    if len(piecs) == 1:
        # end now
        ret = get_min_zero_modu_add(piecs[0], now_map, modu)
        result.append(ret['slove'])
        print ret['slove_map']
        return result
    now_p_pos = length - len(piecs)
    new_piecs = piecs[1:]
    # print new_piecs
    # print piecs[now_p_pos]
    zero_min_ret = get_min_zero_modu_add(piecs[0], now_map, modu)
    result.append(zero_min_ret['slove'])
    return rec_slove_map(new_piecs, zero_min_ret['slove_map'], length, modu, result)


def slove():
    pieces_info = pub_ginfo['gpiecs']
    modu = pub_ginfo['modu']
    base_map = pub_ginfo['gmap']
    print rec_slove_map(pieces_info, base_map, len(pieces_info), modu)


if __name__ == '__main__':
#    print 'aa'
#    print slove()
    print 'main start'
    litter_num = int(sys.argv[1])
    max_num = int(sys.argv[2])
    total_len = mapslove_max_length(jsonret(mstr))
    if total_len < max_num:
        max_num = total_len
    print 'total len:', total_len
    res = mapslove_iter(jsonret(mstr))
    st_time = time.clock()
    unsee = 0
    for i in xrange(0, max_num):
        if i < litter_num:
            res.next()
            continue
        if i % 1000000 == 0:
            print i
        r = res.next()
        if(len(r) != 16):
            unsee += 1
        if checkGameOutNew(r):
            print 'ok game slove', r, i
            break
    print time.clock() - st_time
    print 'end game'
    print unsee
