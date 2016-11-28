#!/usr/bin/env python
#coding=utf8

import simplejson
import urllib2
import urllib
import time
import random
import json
import requests

baseTime = 5


def getdata(url, data):
    post_data = urllib.urlencode(data)
    #req = urllib2.Request(url=url)
    headers = {
        'Host': 'www.qlcoder.com',
        'Connection':'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length':'60',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Cookie':'remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6Im95djl0VGJSRlhzYzE3bmxlUXJVcWc9PSIsInZhbHVlIjoiSmhnNHlBWFlkeW9RWE5ubVpPMFRWdTVlSU90VXZXY2pnSEhNZnRnOTJ6UWkyTVRBNGlJMEk5aUdFNFFhV3pcL1wvdGJZQ2dGZGJEWUJxeVM0aXUyRU16NU5FMEtTOTlCcFhvaTR1XC8xRDkwTGs9IiwibWFjIjoiYTQ2YzMwNjBlNGU5MGE4NjMyNDQ5Mzk2ZjExYjAxZTljMmQ1MzJhNjM2OWFlZjg5NGNiOGExZmRkNzA3NzZiNiJ9; gr_user_id=ded01ff4-d050-4c82-88c0-abbe8248826d; uuid=58134a0c4bc86; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6IjJ3V2g1T1lXQmpqeWpKWDg1UHdrMlE9PSIsInZhbHVlIjoiSFpnbGZydVptRmFNMmV0VUpiQTdBQT09IiwibWFjIjoiNDRhM2U5ZWY5NjgyOGE4MTI2MTkzZDEzY2RhZWI1NDYzOGI3MWFkZmEwYTRmZDNhNGM4ZDhiZDZhNjE3YzRjYyJ9; gr_session_id_80d',
        'Referer': 'http://www.qlcoder.com/task/75b7',
        'Origin': 'http://www.qlcoder.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4'
    }
    print url
    req = urllib2.Request(url=url, data=post_data)
    print "=========="
    soc = urllib2.urlopen(req)
    print "============="
    con = soc.read()
    print con
    soc.close()
    return simplejson.loads(con)


def newGetData(url, data):
    payload = data
    lastC = 'remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6Im95djl0VGJSRlhzYzE3bmxlUXJVcWc9PSIsInZhbHVlIjoiSmhnNHlBWFlkeW9RWE5ubVpPMFRWdTVlSU90VXZXY2pnSEhNZnRnOTJ6UWkyTVRBNGlJMEk5aUdFNFFhV3pcL1wvdGJZQ2dGZGJEWUJxeVM0aXUyRU16NU5FMEtTOTlCcFhvaTR1XC8xRDkwTGs9IiwibWFjIjoiYTQ2YzMwNjBlNGU5MGE4NjMyNDQ5Mzk2ZjExYjAxZTljMmQ1MzJhNjM2OWFlZjg5NGNiOGExZmRkNzA3NzZiNiJ9; gr_user_id=ded01ff4-d050-4c82-88c0-abbe8248826d; uuid=58330e1211a6f; XSRF-TOKEN=eyJpdiI6ImlBYXJpRHZrdGE1a1pDM245WnFyeUE9PSIsInZhbHVlIjoid0JqaHF3YWZISk42WTBRdWU0MFwvQ3Z3b0k3Y0Z2NTd6a0prZWp3TFVmeGkwQStmeFNJYVAxeUZYb0ZcL0l3bW9rSzExcmpJYzBVZUw1MFNQSmZNa0V5UT09IiwibWFjIjoiYzk1N2NmNGIwZTg5OTVkZGI5NTkwNjllMDBjNjYzMjk3MmVmNGJlYjE4Njc0NzI5NWYxODY5ZDNiNGZiNDRkYiJ9; laravel_session=eyJpdiI6IkxXblQzcW50ZjRZVVg1Q3dXRkVIRlE9PSIsInZhbHVlIjoiNWhoT1hGZE1QU3oyM3RkdExxY2JiUnZMS21qRlhxaUlQNTM4XC93YXVlNlV3NGlFQXFGZjk1RTVQSE5VRnRcL1U2MTg1T2J5cDlcL3h4eFQ2Um9Uc0hjMlE9PSIsIm1hYyI6IjJiMDRiYmMwNzkyY2NmMWU3ZGU4NjViNWNiY2FkMTY3ODBhYWZhNmE5MGE4YWUyYzJhODlmZWU4NmIwMjQ1M2QifQ%3D%3D; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6InVndnhCYW5DNlRiOTBNVHFPSHZkUlE9PSIsInZhbHVlIjoielwvaFpYMGRCUUF6UzRSQWNmWDRLMEE9PSIsIm1hYyI6IjZhMzBjNTNjNTkyOWFhN2U3ZDEwNGZjMTgzYjhjNTFlZmE5ZDcwMjg2NzRkNWY1YjNjZTcyOTJmN2ZkNDRiOWUifQ%3D%3D; gr_session_id_80dfd8ec4495dedb=b462268f-11d5-4ce8-b5c9-5665d79416d0; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1478704856,1479041655,1479567059,1479740948; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1480341060'
    headers = {
        'Host': 'www.qlcoder.com',
        'Connection':'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length':'60',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Cookie': lastC,
        'Referer': 'http://www.qlcoder.com/task/75b7',
        'Origin': 'http://www.qlcoder.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4'
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print r

def main():
    url = 'http://www.qlcoder.com/task/52/solve'
    for a in xrange(39505, 43200):
        data = {}
        data['answer'] = str(a)
        data['_token'] = 'c4O5hTqCIu4MwE6w2dgLbTuZOhbIe5FDe6iJ7mnJ'
        ret = newGetData(url, data)
        #ret = getdata(url, data)
        if ret['success'] == 'false':
            print ret
        print ret
        break
        time.sleep(baseTime + random.randint(1, 8))
    print '1'

if __name__ == '__main__':
    main()
