#!/usr/bin/env python
#coding=utf8

import os
#import re


def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


def c_res(cmd):
    result = execCmd(cmd)
    if 'ok game slove' in result:
        print 'ok',result
        return True
    else:
        return False

if __name__ == '__main__':
    import sys
    start_num = 0
    if len(sys.argv)>1:
        start_num = int(sys.argv[1])
    max_num = 200000000
    step = 1000000
    page = 0
    total_page = int(max_num/step) + 1
    print total_page
    for i in xrange(start_num, total_page):
        cmd = 'python /project/python/github/py-fixbugs-tools/test/tmptest.py ' + str(i*step) + ' '+str((i+1)*step)
        ret = c_res(cmd)
        if ret:
            print 'ok'
            break
        print 'last page:', i
    print total_page
    # cmd = 'python /project/python/github/py-fixbugs-tools/test/tmptest.py 0 100'
    # result = execCmd(cmd)
    # if 'end game' in result:
    #     print 'ok'
    # else:
    #     print 'false'
