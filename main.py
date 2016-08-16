#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

import requests
import time
import string
import urllib2
import simplejson

start_time = time.time()


def create_task():
    #从这里传入参数到执行线程中
    result = []
    for i in range(0, 10):
        tmp = {}
        tmp['page'] = i
        result.append(tmp)
    return result


def test(*args, **kwargs):
    if args:
        print args
    if kwargs:
        print 'b' in kwargs
        print kwargs['b']
    return True


class testClass(object):
    def __init__(self, *args, **kwargs):
        self.error_file_path = '/root/work/codeReconstruction/errorlog'
        if args:
            self.args = args
        if kwargs:
            self.kwargs = kwargs

    def test(self, *args, **kwargs):
        page = kwargs['page']
        if not page:
            page = 0
        ret = self.viewUrl(page)
        if not ret:
            #need write into failed file
            print ret

    def viewUrl(self, page):
        try:
            url = 'http://news.leju.com/api/data/gettopnews?time=1463358300&'\
                  + 'size=2&page=' + str(page)
            hd = urllib2.urlopen(url, timeout=30)
            url_res = hd.read()
            if not url_res:
                return False
            res = simplejson.loads(url_res)
            print res
            if 'status' in res and res['status'] is True:
                return True
            else:
                self.errorLogWrite(str(page)+'/n')
        except Exception, e:
            self.errorLogWrite(str(page) + ',' + str(e) + '/n')
        return False

    def errorLogWrite(self, line_data):
        fh = None
        try:
            fh = open(self.error_file_path, 'a')
            fh.write(str(line_data))
        finally:
            if not fh:
                return
            fh.close()


def testThreadQueue():
    from ThreadQueue import ThreadQueue
    t_dict = {'a': '12', "b": '34'}
    t_dict = ('1', '2')
    tc = testClass(t_dict)
    tq = ThreadQueue(work_function=create_task, thread_work_function=tc.test)
    while True:
        if tq.do_work():
            continue
        else:
            break
    print 'ok'


def testDaemon():
    import sys
    from de import Daemon
    daemon = Daemon('/tmp/watch_process.pid', stdout='/tmp/watch_stdout.log')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print 'unknown command'
            sys.exit(2)
        sys.exit(0)
    else:
        print 'usage: %s start|stop|restart' % sys.argv[0]
        sys.exit(2)

def testdb():
    from db import DB
    dbobj = DB()
    print dbobj.query("select * from user_message");

if __name__ == '__main__':
    start_time = time.time()
    #req = testThreadQueue()
    #req = testDaemon()
    req = testdb()
    print req
    used_time = time.time() - start_time
    print used_time
