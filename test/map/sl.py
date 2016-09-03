#!/usr/bin/env python
#coding=utf-8


def liveordie(given_map):
    copymap = {}
    top_l = 0
    bot_l = -0
    left_r = -0
    right_r = 0
    for nme in given_map:
        if nme[0] + 1 > top_l:
            top_l = nme[0] + 1
        if nme[0] - 1 < bot_l:
            bot_l = nme[0] - 1
        if nme[1] + 1 > right_r:
            right_r = nme[1] + 1
        if nme[1] - 1 < left_r:
            left_r = nme[1] - 1
    for i in range(bot_l, top_l+1):
        for j in range(left_r, right_r+1):
            if (i,j) in given_map:
                if lord(given_map, (i, j)) is True:
                    copymap[(i, j)] = True
            else:
                if born(given_map, (i, j)):
                    copymap[(i, j)] = True
    return copymap


def lord(given_map, point):
    num = 0
    if (point[0]-1, point[1]) in given_map:
        num += 1
    if (point[0]+1, point[1]) in given_map:
        num += 1
    if (point[0]-1, point[1]+1) in given_map:
        num += 1
    if (point[0], point[1]+1) in given_map:
        num += 1
    if (point[0]+1, point[1]+1) in given_map:
        num += 1
    if (point[0]-1, point[1]-1) in given_map:
        num += 1
    if (point[0], point[1]-1) in given_map:
        num += 1
    if (point[0]+1, point[1]-1) in given_map:
        num += 1
    if num > 3 or num < 2:
        return False
    else:
        return True


def born(given_map, point):
    num = 0
    if (point[0]-1, point[1]) in given_map:
        num += 1
    if (point[0]+1, point[1]) in given_map:
        num += 1
    if (point[0]-1, point[1]+1) in given_map:
        num += 1
    if (point[0], point[1]+1) in given_map:
        num += 1
    if (point[0]+1, point[1]+1) in given_map:
        num += 1
    if (point[0]-1, point[1]-1) in given_map:
        num += 1
    if (point[0], point[1]-1) in given_map:
        num += 1
    if (point[0]+1, point[1]-1) in given_map:
        num += 1
    if num != 3:
        return False
    else:
        return True

start = {(0,0): True,(0,1): True,(1,1): True,(0,-1): True,(-1,0): True}

rnd = 0
max_rnd = 0

mmax_cre = 0
mmax_rnd = 0

max_cre = len(start)
mapa = start
count = 0
while(len(mapa) != 0):
    count += 1
    mapa = liveordie(mapa)
    rnd+=1
    max_cre = len(mapa)
    max_rnd = rnd
    if max_cre > mmax_cre:
        mmax_cre = max_cre
        mmax_rnd = max_rnd
    if count == 1000:
        break
    #print (max_rnd, max_cre)

print ('----------------result------------')
print (str(mmax_cre) + '-' + str(mmax_rnd))
#print(max_rnd, max_cre, mapa)
