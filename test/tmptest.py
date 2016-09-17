#!/usr/bin/env python
#coding=utf8

# ans_ret = [7875463, 61729516, 2343559, 5545586, 12520119, 41171814, 14185621, 2288994, 11874177, 18108938, 25482199]

# checkcode = 1
# answer_result = list()
# for a in ans_ret:
#     answer_result.append( str(checkcode)+str(a))
#     checkcode += 1

# checkcode = 25
# for ans_r in answer_result:
#     print ans_r,checkcode, str(checkcode+1)
#     print ans_r.startswith(str(checkcode+1))

#     if ans_r.startswith(str(checkcode+1)):
#         t_len = len(str(checkcode+1))
#         print 'trtttttt'
#         print int(ans_r[t_len:])

#print answer_result

import simplejson
import sys


def jsonret(jstr):
    return simplejson.loads(jstr)

mstr_11 = '{"level":11,"modu":"2","map":["1111","1001","1100"],"pieces":["X,X","X,X","XXX,XX.",".X.,XXX","XX,X.,X.","XXXX,.X..",".X,XX,.X"]}'
mstr_12 = '{"level":12,"modu":"2","map":["1101","1011","0101","1111"],"pieces":["..X,XXX","X.,XX","..X,.XX,XX.,.X.","X...,X...,XXXX","XX.,.X.,.XX,..X","X,X",".X,XX","..X,XXX"]}'
mstr = '{"level":13,"modu":"3","map":["0210","0200","1011","2102"],"pieces":["X.,XX,.X",".X,.X,XX",".X,.X,.X,XX","XXXX,.X..",".X,XX,.X,.X","XX,.X","XXX,..X","XX"]}'
mstr_14 = '{"level":14,"modu":"2","map":["0011","1011","0101","0001","1001"],"pieces":["X,X,X,X,X","XX,XX,X.,X.,X.","XX.,.X.,XXX,.X.","XXX,X..","X,X,X","X.,XX,.X","XX,.X","XXXX,.X.."]}'
mstr_15 = '{"level":15,"modu":"3","map":["00220","20111","21101","10200","02022"], "pieces":[".X,XX","XXXX,X...","XX.,.XX,..X,..X,..X","XXX..,..XX.,...XX","...X,XXXX,..X.","XX,X.,X.","XX,.X,.X","XXX,.X.","X.,XX"]}'


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


import itertools


def map_p(l1, l2):
    c = itertools.product(l1, l2)
    result = list()
    for elem in c:
        result.append(str(''.join(elem)))
    return result


def mapsolve(ddict):
    m_map = ddict['map']
    m_modu = ddict['modu']
    m_pieces = ddict['pieces']

    map_row_len = len(m_map)
    map_col_len = len(m_map[0])
    res = list()
    for piec in m_pieces:
        res.append(modu_list_get(piec, map_row_len, map_col_len))
    tt_r = res[0]
    num = 1 * len(res[0])
    for i in xrange(1, len(res)):
        num = num * len(res[i])
        tt_r = map_p(tt_r, res[i])
    return tt_r


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


def mapslove_pieces(ddict):
    m_map = ddict['map']
    m_modu = ddict['modu']
    m_pieces = ddict['pieces']

    map_row_len = len(m_map)
    map_col_len = len(m_map[0])
    res = list()
    for piec in m_pieces:
        res.append(modu_list_get(piec, map_row_len, map_col_len))
    return res


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
    print xyaddr
    xaddr = xyaddr[0]
    yaddr = xyaddr[1]
    modu = int(modu)
    print piec
    print '--------------'
    for x in xrange(0, len(piec)):
        for y in xrange(0, len(piec[x])):
            gmodu[xaddr+x][yaddr+y] = (gmodu[xaddr+x][yaddr+y] + piec[x][y]) % modu
    return gmodu


t1 = ['00', '01', '02', '10', '11', '12', '20', '21', '22'] #x
t2 = ['00', '01', '10', '11', '20', '21'] #xx
t3 = ['00', '01'] #xx,xx,xx
t4 = ['00', '01', '10', '11'] #xx,xx
t5 = ['00', '01', '02', '10', '11', '12']  #x,x
t6 = ['00'] #xxx,xxx,xxx
t7 = ['00', '01', '02'] #x,x,x
t8 = ['00', '10', '20'] #xxx
t9 = ['00', '10'] #xxx,xxx

l1 = t5
l2 = t5
l3 = t9
l4 = t9
l5 = t3
l6 = t2
l7 = t9


def checkGameOut(ginfo, cslove):
    ginfo = gameBaseInfoDecode(ginfo)
    slove_arr = list()
    count = 0
    tmp_list = list()
    if len(ginfo['gpiecs'])*2 != len(cslove):
        print 'out, slove length error'
        return False
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
    for i in xrange(0, len(slove_arr)):
        gmodu_map = gameResultGet(gmodu_map, ginfo['gpiecs'][i], slove_arr[i], gmodu)
    return gameEndCheck(gmodu_map)

pub_ginfo = gameBaseInfoDecode(jsonret(mstr))


def checkGameOutNew(cslove):
    ginfo = pub_ginfo
    slove_arr = list()
    count = 0
    tmp_list = list()
    if len(ginfo['gpiecs'])*2 != len(cslove):
        print 'out, slove length error'
        return False
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
    print gmodu
    print 'start', gmodu_map
    for i in xrange(0, len(slove_arr)):
        gmodu_map = gameResultGet(gmodu_map, ginfo['gpiecs'][i], slove_arr[i], gmodu)
        print gmodu_map
    gret = gameEndCheck(gmodu_map)
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


# print len(res)
#res = mapsolve(jsonret(mstr))
#print res[0]
#print 'total count:', len(res)
#exit(0)

#test itertools get for more
import time
# res = mapslove_iter(jsonret(mstr))
# st_time = time.clock()
# for i in xrange(0, 200000000):
#     if i<50000000:
#         res.next()
#         continue
#     if i%1000000==0:
#         print i
#     if checkGameOutNew(res.next()):
#         print 'ok game slove'
#         break
# print time.clock() - st_time
# print 'end gmae'
# exit(0)


url = 'http://www.qlcoder.com/train/moducheck?solution='


def getdata(url):
    import urllib2
    headers = {'Cookie':'uuid=57b15ad2211ae; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6IkpFb2hheE5aZFk2UG9nNlwvSk1SenlBPT0iLCJ2YWx1ZSI6IlBaV25YTzZ6WnErSStkdmVERTFQdDNUcUpkME9yVGRNNmtFSzBhdTFIVWZqSzRRd3lFaUt2RzdBU0NBSXVXaE9lSXR1Rzh4QSttUStTc0V1anUrTnhLaHhJMEZabmRWbVYzTTJsTFJmZFd3PSIsIm1hYyI6IjBiNmE5Y2ZmODc5MzQ2YzMwOWMxOGQ0ZmFhZjJjNTI4ZDczYjkwM2EzZDBhZWZjYmMzZDRlYjliMGQ4NzlmN2IifQ%3D%3D; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6Ik5YNlJ1bkhCemVuQVVRRithN25QM2c9PSIsInZhbHVlIjoid0dmbjJ5Y0o2bXd1UUI4bklQUzBGQT09IiwibWFjIjoiOWZiNWQ3NzIzNTJiMWYwMzA5YTE5OWVkZDA4MGI0MTkxMzYxZDY5MWY2NWRmMzBjMzQ2MTZiNzQ3ODI2ODEwNiJ9; XSRF-TOKEN=eyJpdiI6IlFyaGJVeU4rZWlzYmx6SmlNUmRCbFE9PSIsInZhbHVlIjoiTVwvYlh5TWVwZERyTDA4ektNcTFxNnp4SG0yXC91c1lydEsxemw1TnlNNXVDT1lObmtONVZrWnhHRWt4dVBBYnRPVE9NUzdUc20yeFBiWUU4MW4yVGRZQT09IiwibWFjIjoiNDhhZTY0OTkzOTM3MTQ3M2UwODVhOTk5OTA5ZmE2Y2Q2ZTM5YTVkNzEzNzliY2Y2YjEwNDgyZTEzOWIwNDRlZiJ9; laravel_session=eyJpdiI6IlpwZms1XC83TnV5QWFwcjlsd2MzaEl3PT0iLCJ2YWx1ZSI6ImhcL0tPK0IzWWZBTlVLV1NINHhsZnVTMUxNY3JuXC9uNHU1cHlJVWo2QVlIVTg4MDNuREpWVVJNVGZlTk1rTk1Pd21MQng2TWZSamFJZk5oTjA0dzR3ekE9PSIsIm1hYyI6IjZjYmYwM2I3YzZkYzhhZjIxYjc5ZGQ1NWUwYWEyYTIwM2FkZmE3OTAzMmM5OWY0NzZkYzgxMjY0ZDhkOWQ3MjkifQ%3D%3D; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1470644113,1471240913; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1471491235'}
    req = urllib2.Request(url=url, headers=headers)
    soc = urllib2.urlopen(req)
    con = soc.read()
    soc.close()
    return con


def checkResult(url):
    #base_url = 'http://www.qlcoder.com/train/moducheck?solution='
    #url = base_url + r
    ret_data = getdata(url)
    if '失败了' in ret_data:
        print 'failed', url
        return False
    print ret_data
    print 'ok', url
    return True


#import time

class doQueueClass(object):
    def __init__(self, *args, **kwargs):
        self.workcomp = False

    def dowork(self):
        return self.workcomp

    def work(self, r):
        if self.workcomp:
            return True
        ret = checkGameOut(jsonret(mstr), r)
        if ret:
            self.workcomp = True
            print 'end game result:', r
            return True
        return False

    def newwork(self, r):
        if self.workcomp:
            return True
        ret = checkGameOutNew(r)
        if ret:
            self.workcomp = True
            print 'end game result:', r
            return True
        return False


def doThreadQueue():
    from ThreadQueue import ThreadQueue
    dqc = doQueueClass()
    tq = ThreadQueue(work_function=create_task_url, thread_work_function=dqc.work)
    while True:
        if tq.do_work():
            if dqc.dowork():
                break
            else:
                continue
    print 'end'


def doThreadQueueNew(max_num):
    from ThreadQueue import ThreadQueue
    dqc = doQueueClass()
    tq = ThreadQueue(work_function=create_iter, thread_work_function=dqc.newwork, max_exec_num=max_num)
    while True:
        if tq.do_work():
            if dqc.dowork():
                break
            else:
                continue
        else:
            break
    print 'end'


def create_iter():
    return mapslove_iter(jsonret(mstr))


def create_task_url():
    res = mapsolve(jsonret(mstr))
     #print ind
    #'1100022002020021'
    rr = res[0:]
    print 'ned hd count:', len(rr)
    return rr

# st_time = time.clock()
# doThreadQueueNew(1000000)
# print time.clock() - st_time

#print len(create_task_url())
#print doThreadQueue()
#exit(0)


def recursive_back_slove(piecs, n=0, tree_result=list()):
    if len(piecs) == len(tree_result):
        tmp = list()
        for i in xrange(0, len(piecs)):
            tmp.append(piecs[i][tree_result[i]])
        if checkGameOutNew(''.join(tmp)):
            return True
        else:
            return False
    else:
        for i in xrange(0, len(piecs[n])):
            if len(tree_result) < len(piecs):
                tree_result.append(i)
            else:
                tree_result[n] = i
            if recursive_back_slove(piecs, n+1, tree_result):
                return tree_result
        return recursive_back_slove(piecs, n-1, tree_result)


import copy


def conflict(piecs, max_len, piec, tree_result):
    if len(tree_result) == max_len:
        #check
        tmp = list()
        for i in xrange(0, max_len-1):
            tmp.append(piecs[i][tree_result[i]])
        for piecs in piec:
            ttmp = copy.copy(tmp)
            ttmp.append(piecs)
            if checkGameOutNew(''.join(ttmp)):
                return True
    return False


def rbs(piecs, n=0, tree_result=tuple()):
    for l in range(len(piecs)):
        # if len(tree_result) == n:
        #     if not conflict(piecs, len(piecs, piecs[n-1]), tree_result):
        #         tree_result
        #         yield rbs(piecs, n-1, tree_result)
        if not conflict(piecs, len(piecs), piecs[n-1], tree_result):
            if len(tree_result) == n:
                print n, 'len tree result eq', tree_result
                yield (l,)
            else:
                for r in rbs(piecs, n, tree_result+(l,)):
                    yield (l,) + r


if __name__ == '__main__':
    #import sys
    #sys.setrecursionlimit(1000000)
    # mapsl = mapslove_pieces(jsonret(mstr))
    # rres = rbs(mapsl, len(mapsl))
    # for i in range(2):
    #     print rres.next()
    #print recursive_back_slove(mapslove_pieces(jsonret(mstr)), 0)

    #exit(0)
    print 'main start'
    litter_num = int(sys.argv[1])
    max_num = int(sys.argv[2])
    total_len = mapslove_max_length(jsonret(mstr))
    if total_len < max_num:
        max_num = total_len
    print 'total len:', total_len
    res = mapslove_iter(jsonret(mstr))
    st_time = time.clock()
    for i in xrange(0, max_num):
        if i < litter_num:
            res.next()
            continue
        if i % 1000000 == 0:
            print i
        r = res.next()
        if checkGameOutNew(r):
            print 'ok game slove', r, i
            break
        break
    print time.clock() - st_time
    print 'end game'
