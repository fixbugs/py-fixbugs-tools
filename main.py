#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-


import requests
import time
import string

start_time = time.time()

character = string.digits + string.ascii_lowercase + '._@ '
res = ''
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36',
}

try:
    url = "http://news.leju.com/api/data/gettaglists?category="
    req = requests.get(url, headers=headers)
    print req
except:
    pass
else:
    print req.url
    print req.text

used_time = time.time()-start_time

print used_time
