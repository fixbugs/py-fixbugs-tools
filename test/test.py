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


def get_pass(pass_md5):
    pass_md5 = pass_md5.lower()
    import hashlib
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
    shoping_arr = dict()
    total_num = 0
    for l in sp_hd:
        sp_ret = l.split(" ")
        method = sp_ret[0]
        sp_ret[2] = sp_ret[2][:-1]
        if method == 'up':
            if sp_ret[2] in shoping_arr:
                shoping_arr[sp_ret[2]] += int(sp_ret[1])
            else:
                shoping_arr[sp_ret[2]] = int(sp_ret[1])
        elif method == 'down':
            if sp_ret[2] in shoping_arr:
                shoping_arr[sp_ret[2]] -= int(sp_ret[1])
        elif method == 'query':
            min_pr = int(sp_ret[1])
            max_pr = int(sp_ret[2])
            for p, num in shoping_arr.items():
                n_price = int(p)
                if n_price > max_pr:
                    continue
                if int(n_price) < int(min_pr):
                    continue
                total_num += int(num)
    #print shoping_arr
    return total_num

#print shopingtaobao()

import hashlib


def rankmd5():
    datestr = '20160812fixbug'
    checkcode = 1
    result = list()
    count = 1
    answer_result = list()
    while True:
        if checkcode >= 999:
            break
        tmpstr = str(datestr)+str(checkcode)+str(count)
        strmd5 = getmd5(tmpstr)

        if strmd5.startswith('000000'):
            answer_result.append(str(checkcode)+str(count))
            result.append(count)
            #t_url = 'http://www.qlcoder.com/train/handsomerank?_token=p5YfP8MPGp8ZXReTa41PmMoA8F9OWiG66AbOqgi1&user=fixbug&checkcode='+str(count)
            print t_url
            #getdata(t_url)
            count = 1
            for ans_r in answer_result:
                if ans_r.startswith(str(checkcode+1)):
                    t_len = len(str(checkcode+1))
                    count = int(ans_r[t_len-1:])
            checkcode += 1
            continue
        count += 1
        if checkcode == 12:
            break
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

print rankmd5()
