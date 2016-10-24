#!/usr/bin/env python
#coding=utf8

import random
import sys
import hashlib
import numpy
import string


# def getFileContent(file_path):
#     import os
#     if not os.path.exists(file_path):
#         return False
#     result = []
#     try:
#         f = open(file_path, 'r')
#         result = f.readlines()
#     finally:
#         f.close()
#     return result

# cont = getFileContent('time_line_res.txt')
# print len(cont)
# for t in cont:
#     print hashlib.md5(t).hexdigest()
# exit(0)

global_digest_list = list()
if sys.version_info[0] == 3:
    print ("Welcome to qlcoder!")
    print ("We find your Python version is python3.X")
    print ("But this script needs to be executed with Python2.X\n")
    exit()

random.seed(10)
limit = 10000000
limit = 1000
vertex_list = numpy.ndarray(limit + 1)
vertex_list = map(lambda ele: [], vertex_list)


def compute_md5(str_list):
    #res_str = reduce(lambda x, y: str(x) + "-" + str(y), str_list)
    res_str = '-'.join(str_list)
    return hashlib.md5(res_str).hexdigest()


def verbose_time_line(vertex_index):
    if len(vertex_list[vertex_index]) == 0:
        global_digest_list.append(hashlib.md5("").hexdigest())
    else:
        vertex_list[vertex_index].reverse()
        if len(vertex_list[vertex_index]) == 1:
            global_digest_list.append(hashlib.md5(vertex_list[vertex_index][0]).hexdigest())
        else:
            global_digest_list.append(compute_md5(vertex_list[vertex_index]))
        vertex_list[vertex_index] = list()


def notify_message(vertex_index, message_str):
    times_count = 2
    notified_vertex_index = times_count * vertex_index
    while notified_vertex_index < limit + 1:
        vertex_list[notified_vertex_index].append(message_str)
        times_count += 1
        notified_vertex_index = times_count * vertex_index

###test
# notify_message(2, 'hello')
# notify_message(2, 'iloveyou')
# notify_message(2, 'heyjuice')
# verbose_time_line(10)
# notify_message(2, 'yoyoyo')
# notify_message(5, 'checknow')
# verbose_time_line(10)
# verbose_time_line(6)
# print global_digest_list
# exit(0)
###test

for i in range(limit):
    r = random.randint(1, limit)
    if i % 3 == 0:
        message_str = ''.join(random.sample(string.ascii_letters, 4))
        notify_message(r, message_str)
    else:
        verbose_time_line(r)

with open('time_line_res.txt', 'w') as ofs:
    for my_str in global_digest_list:
        ofs.write('-')
        ofs.write(my_str)
