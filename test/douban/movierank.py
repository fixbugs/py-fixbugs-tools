#!/usr/bin/env python
#coding=utf-8

import re

def getdata(url):
    import urllib2
    req = urllib2.Request(url=url)
    soc = urllib2.urlopen(req)
    con = soc.read()
    soc.close()
    return con

def ana_html(html):
    sc_reg = 'class=\"rating_num\"[^>]+>([^<]+)</span>'
    regex_matchs = re.findall(sc_reg, html)
    return regex_matchs

def main():
    base_url = 'https://movie.douban.com/top250?start='
    num = 25
    result = list()
    for i in range(0,7):
        tmp_url = base_url + str(num*i) + '&filter='
        print tmp_url
        if i == 6:
            ana_res = ana_html(getdata(tmp_url))
            result.extend(ana_res[0:16])
        else:
            result.extend(ana_html(getdata(tmp_url)))
    ss = 0.0
    print 'result length:',len(result)
    print result
    for r in result:
        ss += float(r)
    return ss

if __name__ == '__main__':
    url = 'https://movie.douban.com/top250'
    #html = getdata(url)
    #print ana_html(html)
    print main()
