#!/usr/bin/env python
#coding=utf8

import simplejson
import sys
import itertools
import time
import copy


def jsonret(jstr):
    return simplejson.loads(jstr)

#725594112 => 125170719
#322486272 => 0001010101120110001100 21473880

#209952000000 => 000001014040120120201022 175951673
#3627970560 =>

mstr_test = '{"level":12,"modu":"2","map":["0000","0000","0001","0100"],"pieces":["X","X"]}'
mstr_11 = '{"level":11,"modu":"2","map":["1111","1001","1100"],"pieces":["X,X","X,X","XXX,XX.",".X.,XXX","XX,X.,X.","XXXX,.X..",".X,XX,.X"]}'
mstr_12 = '{"level":12,"modu":"2","map":["1101","1011","0101","1111"],"pieces":["..X,XXX","X.,XX","..X,.XX,XX.,.X.","X...,X...,XXXX","XX.,.X.,.XX,..X","X,X",".X,XX","..X,XXX"]}'
mstr_13 = '{"level":13,"modu":"3","map":["0210","0200","1011","2102"],"pieces":["X.,XX,.X",".X,.X,XX",".X,.X,.X,XX","XXXX,.X..",".X,XX,.X,.X","XX,.X","XXX,..X","XX"]}'
mstr_14 = '{"level":14,"modu":"2","map":["0011","1011","0101","0001","1001"],"pieces":["X,X,X,X,X","XX,XX,X.,X.,X.","XX.,.X.,XXX,.X.","XXX,X..","X,X,X","X.,XX,.X","XX,.X","XXXX,.X.."]}'
mstr_15 = '{"level":15,"modu":"3","map":["00220","20111","21101","10200","02022"], "pieces":[".X,XX","XXXX,X...","XX.,.XX,..X,..X,..X","XXX..,..XX.,...XX","...X,XXXX,..X.","XX,X.,X.","XX,.X,.X","XXX,.X.","X.,XX"]}'
mstr_16 = '{"level":16,"modu":"2","map":["10100","01000","00111","00110"],"pieces":["X.,X.,XX,.X","XX,.X",".X,XX","X,X","X..,XXX","X..,XXX,XX.,X..","...X.,XXXXX,...X.",".X,XX,X.","XX,XX,X."]}'
mstr_17 = '{"level":17,"modu":"3","map":["11122","21102","10000","01112","11200"],"pieces":["..XX,.XX.,XX..,.X..","X.X.,XXXX,.X..","XXX,.X.,.X.","X...,X.XX,XXX.","X,X,X,X,X",".X...,XXXXX,X..X.","X..,XXX","XXX,X.X,X..","XX,X."]}'
mstr_18 = '{"level":18,"modu":"2","map":["1010","0011","0101","1101","1110"],"pieces":["XX,.X",".X.,.X.,XXX","X.,XX,X.",".X..,XX..,.XXX,.XX.",".X.,XXX",".X..,XX..,XXXX,.X..",".X,.X,XX","X..,X..,XXX,XX.,X..","X.,X.,XX","X.,XX,.X"]}'
mstr_19 = '{"level":19,"modu":"3","map":["0022","2102","1112","1111","2210"],"pieces":[".X,.X,XX,XX","XX,X.,X.","X.,XX","X..,XXX,.X.,.X.","XX,X.","XXX,..X","X.,X.,XX,.X,.X","XXXX","XX,X.","..X.,..X.,XXXX,...X"]}'
mstr_20 = '{"level":20,"modu":"2","map":["111011","001110","001000","110110","110100"],"pieces":["X.X.,XXX.,..XX,..X.","XX.,.X.,XXX,X..","X...,XXXX,.X..,.X..","....XX,XXXXX.,...X..,...X..","X..,X..,XXX","...X.,XXXXX,.X...,.X...","XXX,X..","XXX.,..XX,...X,..XX,..X.",".X,XX","XX,.X,.X"]}'
mstr_21 = '{"level":21,"modu":"3","map":["120212","212222","100220","000112","001210"],"pieces":["XXX.,..X.,..XX","XX,X.","...X,X.XX,XXXX","X.,XX,X.",".X..,XXXX,..XX,...X,...X",".X,XX","...XX,...X.,XXXX.,.X...,.X...","X...,X...,XXX.,..XX,..XX","..X.,.XXX,.XX.,XX..,X...","..X.,..X.,..XX,XXX.,XX..","XX,.X,.X"]}'
mstr_22 = '{"level":22,"modu":"2","map":["00111","11000","10100","01100"],"pieces":[".X..,.XXX,XX..,X...","X..,XXX","X.,XX,X.","..XX,.XX.,XX..,.X..","X..,XXX",".X.,XXX","..X.,XXX.,..XX","XX,.X,XX",".XXX,XX.X","XXX",".X.,XXX,..X"]}'
mstr_23 = '{"level":23,"modu":"3","map":["00102","01112","10202","11212","01112","02202"],"pieces":[".X,XX,X.,X.","...X,...X,..XX,XXX.,X...","....X,XXXXX,X.X..,X....","..X..,..X..,.XX..,XXXX.,...XX",".X.,XXX,XX.,X..,XXX","..X,XXX,..X,..X",".X.,XXX,.XX,XXX,.X.","..X,XXX,X..,X..",".XX.,XXXX,X...","..X,XXX,.X.,.X.",".XX,.XX,XX."]}'
mstr_24 = '{"level":24,"modu":"2","map":["01010","10100","01101","11101","00111","01011"],"pieces":["XX.,.XX","X,X,X,X","X.XX,XXX.,.X..,.XX.","XXX,.X.","XXX..,X.XXX","..X.,XXXX",".X,XX,XX,X.",".XXX,.XX.,..X.,XXX.,..X.","...X,...X,XXXX","..X,XXX","..XX.,XXXXX,XX..X","X..,X..,XXX,.X."]}'
mstr_25 = '{"level":25,"modu":"3","map":["1222","0200","1012","2222","2121"],"pieces":[".X.,.XX,XXX","X.,XX,X.,X.","XXX,..X",".X,XX,X.,XX","XXXX","X.,X.,XX,X.,X.","X..,XXX",".X,XX",".X,XX,X.","X.,X.,X.,XX,.X","X..,X..,XXX",".X,XX,.X"]}'
mstr_26 = '{"level":26,"modu":"4","map":["032200","100310","232330","210230","232333","213230"],"pieces":["XX,.X",".XX,XX.","..X.,..X.,.XXX,XXXX,X...","XXX.,..XX,..X.","..X..,..X..,.XX..,XXXXX,..XX.","...X,.XXX,XX..","XX..,.XXX,.XX.,.X..","XXX,XXX,.XX,XX.,.X.",".XX,..X,XXX,XX.,.X.","..XX.,.XXXX,.XX..,XX...",".X...,XXXXX,...XX,...XX",".XX,XX.,XX.,.X.,.X."]}'

mstr = mstr_26


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

jmstr = jsonret(mstr)


def pubGlobalInfo():
    return gameBaseInfoDecode(jmstr)


def checkGameOutNew(cslove):
    #ginfo = pubGlobalInfo()
    ginfo = copy.deepcopy(pub_ginfo)
    slove_arr = list()
    tmp_list = list()
    count = 0
    cslove_len = len(cslove)
    # if len(ginfo['gpiecs'])*2 != cslove_len:
    #     print 'out, slove length error'
    #     return False
    ########################
    # gmodu_map = ginfo['gmap']
    # gmodu = ginfo['modu']
    # for i in xrange(0, cslove_len):
    #     tmp_list.append(int(cslove[i]))
    #     if count == 1:
    #         count = 0
    #         now_p = (i+1)/2 - 1
    #         gmodu_map = gameResultGet(gmodu_map, ginfo['gpiecs'][now_p], tmp_list, gmodu)
    #         tmp_list = list()
    #         continue
    #     count += 1
    ######################
    for i in xrange(0, cslove_len):
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
    slove_arr_len = len(slove_arr)
    for i in xrange(0, slove_arr_len):
        count += 1
        gmodu_map = gameResultGet(gmodu_map, ginfo['gpiecs'][i], slove_arr[i], gmodu)
        #can check has next
    gret = gameEndCheck(gmodu_map)
    if gret:
        return cslove
    else:
        return gret


def gameEndCheck(gmodu_map):
    xlen = len(gmodu_map)
    for x in xrange(0, xlen):
        ylen = len(gmodu_map[x])
        for y in xrange(0, ylen):
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
    result['slove_map'] = gameResultGet(now_map, piec, result['slove'], modu)
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
    modu_info = jsonret(mstr)
    total_len = mapslove_max_length(modu_info)
    if total_len < max_num:
        max_num = total_len
    print 'total len:', total_len
    res = mapslove_iter(modu_info)
    st_time = time.clock()
    for i in xrange(0, max_num):
        if i < litter_num:
            res.next()
            continue
        if i % 100000 == 0:
            print i
        r = res.next()
        if checkGameOutNew(r):
            print 'ok game slove', r, i
            break
    print time.clock() - st_time
    print 'end game'
