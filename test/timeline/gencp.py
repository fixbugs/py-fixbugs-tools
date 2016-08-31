import random
import string
import sys
if sys.version_info[0] == 3:
    print ("Welcome to qlcoder!")
    print ("We find your Python version is python3.X")
    print ("But this script needs to be executed with Python2.X\n")
    exit()

random.seed(10)
limit = 10000000
# out = open('timeline.txt', 'w')
# for i in range(limit):
#     r = random.randint(1, limit)
#     if i % 3 == 0:
#         out.write('p ' + str(r) + ' ' + ''.join(random.sample(string.ascii_letters, 4)) + '\r\n')
#     else:
#         out.write('v ' + str(r) + '\r\n')

import math
import hashlib


def string_md5(c_str):
    return hashlib.md5(c_str).hexdigest()


def isPrime(n):
    return not [i for i in range(2, int(math.sqrt(n)) + 1) if n%i == 0]


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


v_result = list()
all_data = list()
site_arr = [0] * limit
for i in xrange(limit):
    tmp_d = dict()
    r = random.randint(1, limit)
    if i % 10000 == 0:
        print i
        print ' ----------------------'
    if i % 3 == 0:
        #p
        tmp_d['method'] = 'p'
        tmp_d['person'] = int(r)
        tmp_d['content'] = ''.join(random.sample(string.ascii_letters, 4))
        all_data.append(tmp_d)
    else:
        tmp_d['method'] = 'v'
        tmp_d['person'] = int(r)
        all_data.append(tmp_d)
        last_site_num = site_arr[r]
        site_arr[r] = i
        speak_str = list()
        if isPrime(int(r)):
            continue
        for x in all_data[i-1:last_site_num-1:-1]:
            if x['method'] == 'v':
                if x['person'] == tmp_d['person']:
                    break
            else:
                if tmp_d['person'] == x['person']:
                    continue
                if tmp_d['person'] % x['person'] == 0:
                    print 'add content'
                    speak_str.append(x['content'])
        if len(speak_str):
            v_result.append(string_md5('-'.join(speak_str)))


print string_md5('-'.join(v_result))
