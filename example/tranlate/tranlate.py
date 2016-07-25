#/usr/bin/env python
#coding=utf8

import httplib
import md5

import urllib
import random
import simplejson


class Tranlate(object):

    def __init__(self, appid, secretKey, fromLang='en', toLang='zh'):
        self._appid = appid
        self._secretKey = secretKey
        self._url = '/api/trans/vip/translate'
        self._thost = 'api.fanyi.baidu.com'
        self._fromLang = fromLang if True else 'en'
        self._toLang = toLang if True else 'zh'
        self._getsalt()

    def _getsalt(self):
        self._salt = random.randint(32768, 65536)

    def setQueryString(self, qString):
        self._qstring = qString

    def getResult(self, qString=None):
        if qString:
            q = qString
        else:
            q = self._qstring
        if not self._qstring:
            return False
        sign = self._appid + q + str(self._salt) + self._secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = self._url + '?appid=' + self._appid + '&q=' + urllib.quote(q) + '&from=' + self._fromLang + '&to=' + self._toLang + '&salt=' + str(self._salt) + '&sign=' + sign
        try:
            httpClient = httplib.HTTPConnection(self._thost)
            httpClient.request('GET', myurl)
            #response是HTTPResponse对象
            response = httpClient.getresponse()
            res = response.read()
            ret = simplejson.loads(res)
            return ret['trans_result'][0]['dst']
        except Exception, e:
            raise e
        finally:
            if httpClient:
                httpClient.close()
        return False

appid = '20160724000025705'
secretKey = 'sLxLk0lYnHPL1wZ_e5_x'

tcls = Tranlate(appid, secretKey)
tcls.setQueryString('chinese english apple')
print tcls.getResult()

# httpClient = None
# myurl = '/api/trans/vip/translate'
# q = 'chinese apple'
# fromLang = 'en'
# toLang = 'zh'
# salt = random.randint(32768, 65536)

# sign = appid+q+str(salt)+secretKey
# m1 = md5.new()
# m1.update(sign)
# sign = m1.hexdigest()
# myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

# try:
#     httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
#     httpClient.request('GET', myurl)

#     #response是HTTPResponse对象
#     response = httpClient.getresponse()
#     res = response.read()
#     ret = simplejson.loads(res)
#     print ret
#     print ret['trans_result'][0]['dst']
# except Exception, e:
#     print e
# finally:
#     if httpClient:
#         httpClient.close()
