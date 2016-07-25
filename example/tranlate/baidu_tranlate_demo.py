#/usr/bin/env python
#coding=utf8

import httplib
import md5

import urllib
import random
import simplejson

appid = '20160724000025705'
secretKey = 'sLxLk0lYnHPL1wZ_e5_x'

httpClient = None
myurl = '/api/trans/vip/translate'
q = 'chinese apple'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

try:
    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    res = response.read()
    ret = simplejson.loads(res)
    print ret
    print ret['trans_result'][0]['dst']
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
