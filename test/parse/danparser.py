#!/usr/bin/env python
#coding=utf-8

import urllib2
import time

def getdata(url):
    req = urllib2.Request(url=url)
    soc = urllib2.urlopen(req)
    con = soc.read()
    soc.close()
    return con


start = {}
counter = {}
stop = {}
web = {}
for numb in range (3,11):
    start[numb] = 0;
    counter[numb] = 0;
    stop[numb] = 0;
    url1 = "http://www.qlcoder.com/train/spider3/" + str(numb)
    web[numb] = getdata(url1)
total = 0
for numb in range (3,11):
    total = total + stop[numb]
time.sleep(5)
while(total<8):
    for numb in range (3,11):
        url1 = "http://www.qlcoder.com/train/spider3/" + str(numb)
        webdectemp = getdata(url1)
        if(webdectemp != web[numb]):
            if(start[numb] == 0):
                start[numb] = 1
                web[numb] = webdectemp
            else:
                stop[numb] = 1
        else:
            if(start[numb] == 1 and stop[numb] == 0):
                counter[numb] = counter[numb] + 1
    time.sleep(5)
    total = 0
    for numb in range (3,11):
        total = total + stop[numb]
    print("start:",start)
    print("counter:",counter)
    print("stop:",stop)

print("counter:",counter)#此处最好再sort一下
print("-----------------")
print(counter.sort())
#'1-2-10-9-6-5-4-3-7-8'
