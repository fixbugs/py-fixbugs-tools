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

def jsonret(jstr):
    import simplejson
    return simplejson.loads(jstr)

mstr_11 = '{"level":11,"modu":"2","map":["1111","1001","1100"],"pieces":["X,X","X,X","XXX,XX.",".X.,XXX","XX,X.,X.","XXXX,.X..",".X,XX,.X"]}'
mstr_12 = '{"level":12,"modu":"2","map":["1101","1011","0101","1111"],"pieces":["..X,XXX","X.,XX","..X,.XX,XX.,.X.","X...,X...,XXXX","XX.,.X.,.XX,..X","X,X",".X,XX","..X,XXX"]}'
mstr = '{"level":13,"modu":"3","map":["0210","0200","1011","2102"],"pieces":["X.,XX,.X",".X,.X,XX",".X,.X,.X,XX","XXXX,.X..",".X,XX,.X,.X","XX,.X","XXX,..X","XX"]}'

def modu_list_get(piec, row_len, col_len):
    result_list = list()
    if ',' in piec:
        piec_list = piec.split(',')
        p_row_len = len(piec_list)
        p_col_len = len(piec_list[0])
        max_row = row_len - p_row_len
        max_col = col_len - p_col_len
        for r in range(0, max_row+1):
            for l in range(0, max_col+1):
                result_list.append(str(r)+str(l))
    else:
        max_row = row_len - 1
        max_col = col_len - len(piec)
        for r in range(0, max_row+1):
            for l in range(0, max_col+1):
                result_list.append(str(r)+str(l))
    return result_list

def map_p(l1, l2):
    import itertools
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
    for i in range(1, len(res)):
        num = num * len(res[i])
        tt_r = map_p(tt_r, res[i])
    return tt_r

#print mapsolve( jsonret(mstr) )


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


# res = list()
# for i1 in l1:
#     for i2 in l2:
#         for i3 in l3:
#             for i4 in l4:
#                 for i5 in l5:
#                     for i6 in l6:
#                         for i7 in l7:
#                             res.append(i1+i2+i3+i4+i5+i6+i7)

# print len(res)
res = mapsolve(jsonret(mstr))
print 'total count:', len(res)

url = 'http://www.qlcoder.com/train/moducheck?solution='


def getdata(url):
    import urllib2
    headers = {'Cookie':'uuid=57b15ad2211ae; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6IkpFb2hheE5aZFk2UG9nNlwvSk1SenlBPT0iLCJ2YWx1ZSI6IlBaV25YTzZ6WnErSStkdmVERTFQdDNUcUpkME9yVGRNNmtFSzBhdTFIVWZqSzRRd3lFaUt2RzdBU0NBSXVXaE9lSXR1Rzh4QSttUStTc0V1anUrTnhLaHhJMEZabmRWbVYzTTJsTFJmZFd3PSIsIm1hYyI6IjBiNmE5Y2ZmODc5MzQ2YzMwOWMxOGQ0ZmFhZjJjNTI4ZDczYjkwM2EzZDBhZWZjYmMzZDRlYjliMGQ4NzlmN2IifQ%3D%3D; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6IittXC9wRXJKWkUyV1NHeVJpVHNsYkVBPT0iLCJ2YWx1ZSI6InJIK0lNeHp5b0FIYk4wWlUyaTVCTUE9PSIsIm1hYyI6ImM0ZWM4MGI5ZjZiOTRkMDFjMDhiMTRmMGVhMjA5NGMwYjI3ODUxYWJkZDcxZGI5MTNmNzUzNjQzMjk3MjQ1OWEifQ%3D%3D; XSRF-TOKEN=eyJpdiI6InBZZGF6MVhONGVcL3JXbVJcL1ZITFI4UT09IiwidmFsdWUiOiJ1Zk9paUpXSDdGWUg3NFdxRVZYUUs0ck9ibjZ1NzhhUzZDR3NFaUZUVUg4UTNoUkJCMVZGa3ZMdEhzS0tnZTJ0YzlzRFJaMW9iZkQyNmthaklDR0hIdz09IiwibWFjIjoiYjVkNmMzZTEyOTU2OTQwMmMzODU4MGEyZWY2Yjk1YzQwMDQyMGIzZGE0YTU4OTI5NTc2Y2YzMDE5MzUxN2ZkOCJ9; laravel_session=eyJpdiI6InZ6d0I2SzR4OTBWa0puajlqeCt3aGc9PSIsInZhbHVlIjoiTE9Lb3Zqb2VHYnNrK3E4N3BSbHMyaDB5dHZDMEZ5QXhrZVdrYm42K3dJMjhmVE9oWGdGbksyeW1BTmNUMGdLOVFWaXVyVWFaRnpMVVczaTgwN1lrU2c9PSIsIm1hYyI6ImQ1NjhmYTRjNjU3Y2M5N2M3ZmNlYTVhNTEzNjc0YzljOTEwOWE3YjBmYjIzNGNlYTEwYmE1YjUwMjRiODI2OTkifQ%3D%3D; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1470644113,1471240913; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1471481801'}
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


import time


class doQueueClass(object):
    def __init__(self, *args, **kwargs):
        self.workcomp = False

    def dowork(self):
        return self.workcomp

    def work(self, r):
        if self.workcomp:
            return True
        baseurl = 'http://www.qlcoder.com/train/moducheck?solution='
        ret = getdata(baseurl+r)
        if '失败了' in ret:
            print 'failed', r
            return False
        else:
            if '请先登陆' in ret:
                time.sleep(2)
                ret = getdata(baseurl+r)
                if '失败了' in ret:
                    print 'failed',r
                    return False
            self.workcomp = True
            print 'ok', ret, r
            return True

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

def create_task_url():
    res = mapsolve(jsonret(mstr))
    ind = res.index('0000022000122122')
    #print ind
    #'1100022002020021'
    rr = res[ind:]
    print 'ned hd count:',len(rr)
    return rr

#print len(create_task_url())
print doThreadQueue()
exit(0)

i = 0

for r in res:
    i += 1
    #ret_data = getdata(url+r)
    if not checkResult(url+r):
        print 'failed', r
    else:
        print 'ok', url+r
        break
