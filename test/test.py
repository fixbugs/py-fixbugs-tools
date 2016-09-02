#!/usr/bin/env python
#coding=utf8


def get_data(num=2333):
    count = 0
    for i in range(2, 10000):
        if i % 2 == 0 or i % 3 == 0:
            count += 1
        if count == num:
            return i
    return False

#print get_data()


def box(data, max_num):
    box_arr = []
    tag_arr = []
    d_len = len(data)
    for i in range(0, max_num):
        tmp = dict()
        tmp['weight'] = 0
        tmp['mark'] = list()
        for j in range(0, d_len):
            tmp['mark'].append(False)
        tag_arr.append(tmp)
    for i in range(0, d_len):
        j = max_num - 1
        while True:
            if not j:
                break
            if j < data[i]:
                break
            if tag_arr[j]['weight'] < tag_arr[j - data[i]]['weight'] + data[i]:
                tag_arr[j]['weight'] = tag_arr[j - data[i]]['weight'] + data[i]
                for k in range(0, d_len):
                    tag_arr[j]['mark'][k] = tag_arr[j - data[i]]['mark'][k]
                tag_arr[j]['mark'][i] = True
            j = j - 1
    flag = 1
    for i in range(0, d_len):
        if(flag and tag_arr[max_num - 1]['mark'][i]):
            box_arr.append(i + 1)
            flag = 0
            continue
        if(tag_arr[max_num - 1]['mark'][i]):
            box_arr.append(i + 1)
    result = dict()
    result['weight'] = tag_arr[max_num - 1]['weight']
    result['box_link'] = '-'.join(map(str, box_arr))
    return result

# hd_arr = [509, 838, 924, 650, 604, 793, 564, 651, 697, 649, 747, 787, 701, 605, 644]
# max_num = 5000
# print box(hd_arr, max_num)
# exit(0)

import hashlib


def get_pass(pass_md5):
    pass_md5 = pass_md5.lower()
    for i in range(1990, 2016):
        for j in range(1, 12):
            for k in range(1, 31):
                y = str(i)
                m = '0'+str(j) if j < 10 else str(j)
                d = '0'+str(k) if k < 10 else str(k)
                tmp_str = y+m+d
                if hashlib.md5(tmp_str).hexdigest() == pass_md5:
                    return tmp_str

#print get_pass('7E38890B870934B126F66857ED6B57B9')


def hotshare():
    res = getFileContent('friends.txt')
    print res


'''
根据文件路径获取文件内容
@param file_path string 文件路径
@return False or Dict 返回文件内容数组或者False
'''
def getFileContent(file_path):
    import os
    if not os.path.exists(file_path):
        return False
    result = []
    try:
        f = open(file_path, 'r')
        result = f.readlines()
    finally:
        f.close()
    return result

#print hotshare()


def shopingtaobao():
    sp_hd = getFileContent('taobao2.txt')
    shoping_arr = [0]*100001
    total_num = 0
    now_num = 1
    count = 1
    for l in sp_hd:
        now_num += 1
        sp_ret = l.split(" ")
        method = sp_ret[0]
        sp_ret[2] = sp_ret[2][:-1]
        if method == 'up':
            shoping_arr[int(sp_ret[2])] += int(sp_ret[1])
        elif method == 'down':
            shoping_arr[int(sp_ret[2])] -= int(sp_ret[1])
        elif method == 'query':
            min_pr = int(sp_ret[1])
            max_pr = int(sp_ret[2])
            total_num += sum(shoping_arr[min_pr:max_pr+1])
            #print now_num, total_num, 'total_end', min_pr, max_pr
            count += 1
            if count % 1000 == 0:
                print now_num, total_num, 'total_end', min_pr, max_pr
            # for p, num in shoping_arr.items():
            #     n_price = int(p)
            #     if n_price > max_pr:
            #         continue
            #     if int(n_price) < int(min_pr):
            #         continue
            #     total_num += int(num)
    #print shoping_arr
    return total_num

print shopingtaobao()
exit(0)


def rankmd5():
    datestr = '20160813fixbug'
    checkcode = 999
    result = list()
    count = 1
    answer_result = list()
    #old_ans_result = ['17875463', '261729516', '32343559', '45545586', '512520119', '641171814', '714185621', '82288994', '911874177', '1018108938', '1125482199', '129780706', '1366327270', '1440056777', '152184421', '1621773862', '17875463', '189586934']
    #answer_result = old_ans_result
    while True:
        #if len(old_ans_result) >= checkcode:
         #   checkcode += 1
         #   continue
        if checkcode >= 1001:
            break
        tmpstr = str(datestr)+str(checkcode)+str(count)
        strmd5 = getmd5(tmpstr)

        if strmd5.startswith('000000'):
            answer_result.append(str(checkcode)+str(count))
            result.append(count)
            t_url = 'http://www.qlcoder.com/train/handsomerank?_token=p5YfP8MPGp8ZXReTa41PmMoA8F9OWiG66AbOqgi1&user=fixbug&checkcode='+str(count)
            #print t_url
            #if checkcode >= 21:
                #getdata(t_url)
            count = 1
            for ans_r in answer_result:
                if ans_r.startswith(str(checkcode+1)):
                    t_len = len(str(checkcode+1))
                    count = int(ans_r[t_len:])
            checkcode += 1
            continue
        count += 1
        # for a in answer_result:
        #     if a.startswith((str)checkcode):
        #         break
    print result
    print answer_result


def getmd5(str):
    return hashlib.md5(str).hexdigest()


def getdata(url):
    import urllib
    print url
    f = urllib.urlopen(url)
    return True

#print rankmd5()

#print getFileContent('tt.txt')


def lineget():
    import numpy as np
    x, y = np.loadtxt('tt.txt', unpack=True)
    print '-'.join(map(str, np.polyfit(x, y, 1)))

#print lineget()


def lineget2():
    import StringIO
    import urllib2
    import numpy as np
    d = urllib2.urlopen("http://www.qlcoder.com/download/145622513871043.txt").read().decode("utf-8")

    arr = np.genfromtxt(StringIO.StringIO(d), delimiter=" ")
    z1 = np.polyfit(arr[:,0], arr[:,1], 5)
    print z1
    print ':'.join([str(i) for i in z1])

#print lineget2()


def moduslove():
    mstr = '{"level":3,"modu":"2","map":["100","010","011"],"pieces":["XXX","X",".X,XX","X,X,X"]}'
    import simplejson
    m_dict = simplejson.loads(mstr)
    m_map = m_dict['map']
    m_pieces = m_dict['pieces']
    for m in m_map:
        print m
    m_pee = list()
    for mp in m_pieces:
        m_pee.append(getmodulist(mp))
    print m_pee


def getmodulist(mstr):
    if ',' in mstr:
        res = list()
        m_arr = mstr.split(',')
        for m in m_arr:
            res.append(getmodulistpstring(m))
        return res
    else:
        return getmodulistpstring(mstr)


def getmodulistpstring(pstring):
    mp_list = list(pstring)
    for k in range(0, len(mp_list)):
        if mp_list[k] == 'X':
            mp_list[k] = '1'
        else:
            mp_list[k] = '0'
    return ''.join(mp_list)


#print moduslove()

def testfunc():
    for i in range(0, 4):
        if i % 2 == 0:
            yield (i,)
        else:
            yield (i,) + (i, 1)
