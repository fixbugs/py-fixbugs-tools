#!/usr/bin/env python
#coding=utf8

ans_ret = [7875463, 61729516, 2343559, 5545586, 12520119, 41171814, 14185621, 2288994, 11874177, 18108938, 25482199]

checkcode = 1
answer_result = list()
for a in ans_ret:
    answer_result.append( str(checkcode)+str(a))
    checkcode += 1

checkcode = 25
for ans_r in answer_result:
    print ans_r,checkcode, str(checkcode+1)
    print ans_r.startswith(str(checkcode+1))

    if ans_r.startswith(str(checkcode+1)):
        t_len = len(str(checkcode+1))
        print 'trtttttt'
        print int(ans_r[t_len:])
    #checkcode += 1

print answer_result
