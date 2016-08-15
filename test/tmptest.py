#!/usr/bin/env python
#coding=utf8

# ans_ret = [7875463, 61729516, 2343559, 5545586, 12520119, 41171814, 14185621, 2288994, 11874177, 18108938, 25482199]

# checkcode = 1
# answer_result = list()
# for a in ans_ret:
#     answer_result.append( str(checkcode)+str(a))
#     checkcode += 1

# checkcode = 25
# for ans_r in answer_result:
#     print ans_r,checkcode, str(checkcode+1)
#     print ans_r.startswith(str(checkcode+1))

#     if ans_r.startswith(str(checkcode+1)):
#         t_len = len(str(checkcode+1))
#         print 'trtttttt'
#         print int(ans_r[t_len:])
    #checkcode += 1

#print answer_result


# 111
# ---
# 11
# 10
# 10
# ---
# 11
# ---
# 11
# ---
# 11
# 10
# 10
# ---
# 110
# 011

t1 = ['00', '01', '02', '10', '11', '12', '20', '21', '22'] #x
t2 = ['00', '01', '10', '11', '20', '21'] #xx
t3 = ['00', '01'] #xx,xx,xx
t4 = ['00', '01', '10', '11'] #xx,xx
t5 = ['00', '01', '02', '10', '11', '12']  #x,x
t6 = ['00'] #xxx,xxx,xxx
t7 = ['00', '01', '02'] #x,x,x
t8 = ['00', '10', '20'] #xxx
t9 = ['00', '10'] #xxx,xxx

l1 = t5
l2 = t5
l3 = t9
l4 = t9
l5 = t3
l6 = t2
l7 = t9


res = list()
for i1 in l1:
    for i2 in l2:
        for i3 in l3:
            for i4 in l4:
                for i5 in l5:
                    for i6 in l6:
                        for i7 in l7:
                            res.append(i1+i2+i3+i4+i5+i6+i7)

print len(res)


url = 'http://www.qlcoder.com/train/moducheck?solution='


def getdata(url):
    import urllib2
    import urllib
    headers = {'Cookie':'uuid=57a9e1be7aabd; XSRF-TOKEN=eyJpdiI6Ikdrbkc5Wk1pZUZSWmtGa25MN1E4TEE9PSIsInZhbHVlIjoiVVdQeFpnWnoxSkdadGJ6MUkyU3pzejgwK2p2REtXeW9yU3hIdkhtSUk3bWp2ZkdrNUZ2UEJDYlNERUZsb1JrVlJ4enI2SDBOeGJpdzluYmtJTVVIUmc9PSIsIm1hYyI6IjI1ODgyZjlkNDMyZmQ4ZWI0ZWZlNjdiM2E2MWNjZjNjOWI1ZTM4ODY5MTYzZGI1ZWQyMjQ0NmJhZDRkOWFhODAifQ%3D%3D; laravel_session=eyJpdiI6IjZ2SzM3ZU8xSXZnaThTNnk2Q2ZZVUE9PSIsInZhbHVlIjoiNmc2XC94M1Rzc2RBY29MajR3XC9uU2JtRVpFTEZEUFpXXC9mRFJHUEg4VVZvK1IzSHhTQkxoRldSN0NtdEVkWENqTWZPQThJaUdad2lXV1k3VEgyM1lBSEE9PSIsIm1hYyI6IjI4Njg4ZmMxZmRkNTYwY2MyYmRkZjc5MDE5OTlkOGEwNGFkNWU2YzcxODI5YjE0ZmVhMjU2OGQ4NGU1MjMxOWIifQ%3D%3D; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6ImxucmpDdW9XSlc3YlBxRmVZM01wZHc9PSIsInZhbHVlIjoiNGFxclVCMENcLzFzT1BCUzUrRUQ1dmc9PSIsIm1hYyI6IjBlZGMzMWU5Njk1MzM1OGQ0ZTZiOGEyMzRiNGRlNWM1NDYzYmIzOTJkZTE3NmUwZTczZGY2NGRjZmRkMjI2Y2IifQ%3D%3D; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1470750046,1470751084,1470751138,1470751188; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1471271412'}
    req = urllib2.Request(url=url, headers=headers)
    soc = urllib2.urlopen(req)
    con = soc.read()
    soc.close()
    return con

i = 0

for r in res:
    i += 1
    ret_data = getdata(url+r)
    if '失败了' in ret_data:
        print 'failed', i
    else:
        print 'ok'
        print url+r
        break

