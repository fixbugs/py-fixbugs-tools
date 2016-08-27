#!/usr/bin/env python
#coding=utf8

import hashlib
import math


def string_md5(c_str):
    return hashlib.md5(c_str).hexdigest()


def factors(n):
    f, fs = 3, []
    while n % 2 == 0:
        fs.append(2)
        n /= 2
        while f * f <= n:
            while n % f == 0:
                fs.append(f)
                n /= f
            f += 2
    if n > 1:
        fs.append(n)
    return list(set(fs))


def isPrime(n):
    return not [i for i in range(2, int(math.sqrt(n)) + 1) if n%i == 0]


def nsqrt(n):
    return n**0.5


def primeFactors(n):
    n = n*2
    x = [i for i in range(2, int(nsqrt(n)) + 1) if isPrime(i) and n%i == 0]
    print n/i
    y = [n/i for i in x if i not in x and isPrime(n/i)]
    if not sum([x, y], []):
        return [n]
    else:
        print x,y
        return sum([x, y], [])


def bPrime(n):
    if isPrime(n):
        return [n]
    else:
        x = 2
        while x <= int(n/2):
            if n%x==0:
                return [x] + bPrime(n/x)
            x = x+1


def numPrimeConb(n):
    return list(set(bPrime(n)))


print numPrimeConb(9999)

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


def formatData():
    all_data = list()
    file_data = getFileContent('timeline.txt')
    v_result = list()
    for i in xrange(len(file_data)):
        tmp_d = dict()
        sp_ret = file_data[i].split(" ")
        method = sp_ret[0]
        person = sp_ret[1]
        if method == 'p':
            tmp_d['method'] = 'p'
            tmp_d['person'] = int(person)
            tmp_d['content'] = sp_ret[2][0:-2]
        else:
            tmp_d['method'] = 'v'
            tmp_d['person'] = int(person)
        all_data.append(tmp_d)
    for i in xrange(len(all_data)):
        if i%10000 == 0:
            print i
        a = all_data[i]
        if a['method'] == 'v':
            #search, add v_result
            speak_str = list()
            for x in all_data[i:0:-1]:
                if x['method'] == 'v':
                    #check_self
                    if x['person'] == a['person']:
                        break
                else:
                    if a['person'] == x['person']:
                        continue
                    if a['person']%x['person'] == 0:
                        speak_str.append(x['content'])
            if len(speak_str):
                v_result.append(string_md5('-'.join(speak_str)))
        else:
            pass
    return string_md5('-'.join(v_result))


print formatData()
