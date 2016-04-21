#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

import requests
import time
import string

start_time = time.time()

## test requests module
# character = string.digits + string.ascii_lowercase + '._@ '
# res = ''
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36',
# }

# try:
#     url = "http://news.leju.com/api/data/gettaglists?category="
#     req = requests.get(url, headers=headers)
#     print req
# except:
#     pass
# else:
#     print req.url
#     print req.text

def create_task():
    result = []
    for i in range(0,81):
        tmp = {}
        tmp['page'] = i
        result.append(tmp)
    return result

def test(*args, **kwargs):
    if args:
        print args
    if kwargs:
        print kwargs.has_key('b')
        print kwargs['b']
    return True

class testClass(object):
    def __init__(self,*args,**kwargs):
        self.error_file_path = '/root/work/codeReconstruction/errorlog'
        if args:
            self.args = args
        if kwargs:
            self.kwargs = kwargs

    def test(self,*args,**kwargs):
        page =  kwargs['page']
        if not page:
            page = 0
        ret =self.viewUrl(page)
        if not ret:
            #need write into failed file
            print ret

    def viewUrl(self,page):
        try:
            #url = 'http://admin.lm.leju.com/api/article/getArticlePublish?page='+ str(page)
            url = 'http://admin.lm.leju.com/test/test/testacticlepublish?page='+ str(page)
            url_res = urllib2.urlopen(url,timeout=30).read()
            if not url_res:
                return False
            res = simplejson.loads(url_res)
            if res.has_key('status') and res['status'] == True:
                print res
                return True
            else:
                self.errorLogWrite(str(page)+'/n')
        except Exception,e:
            self.errorLogWrite(str(page)+ ',' + str(e) + '/n')
            # print "---view url exception start---"
            # print e
            # print "---view url exception end---"
        return False

    def errorLogWrite(self,line_data):
        print self.error_file_path
        try:
            f = open(self.error_file_path,'a')
            f.write(str(line_data))
        finally:
            f.close()

def testThreadQueue():
    from ThreadQueue import ThreadQueue
    t_dict ={'a':'12',"b":'34'}
    t_dict = ('1','2')
    tc = testClass(t_dict)
    tq = ThreadQueue(work_function=create_task,thread_work_function=tc.test)
    print tq.add_tasks()
    print tq.getWorkingQueue()
    #print 'end'
    #exit(0)
    print 'end+1'
    while True:
        if tq.do_work():
            continue
        else:
            break
    print 'ok'


used_time = time.time()-start_time

print used_time

if __name__ == '__main__':
    start_time = time.time()
    req = testThreadQueue()
    print req
    used_time = time.time() - start_time
    print used_time
