#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


MAXX = 1000
MAXY = 1000

listArr = []


class ball(object):
    def __init__(self, initX, initY, spX, spY):
        self._nowX = initX
        self._nowY = initY
        self._nowSpX = spX
        self._nowSpY = spY
        self._spSQ = 0
        self.countSpeedSQ()

    def countEnd(self, timePass):
        self._nowX += timePass * self._nowSpX
        self._nowY += timePass * self._nowSpY

    def setNewSpeed(self, newX, newY):
        self._nowSpX = newX
        self._nowSpY = newY
        self.countSpeedSQ()

    def countSpeedSQ(self):
        self._spSQ = math.sqrt(pow(abs(self._nowSpX), 2) + pow(abs(self._nowSpY), 2))
        if self._nowSpX < 0 and self._nowSpY > 0 or self._nowSpX > 0 and self._nowSpY < 0:
            self._spSQ = -1 * self._spSQ

    def prints(self):
        print 'print self ball START'
        print self._nowX, self._nowY
        print self._nowSpX, self._nowSpY
        print self._spSQ
        print 'print ball END'

    def getNextChangeTime(self):
        xtime = 0
        ytime = 0
        self.prints()
        if self._nowSpX > 0:
            if self._nowX < MAXX/2:
                #right
                xtime = float((MAXX - self._nowX)/self._nowSpX)
            else:
                #left
                xtime = float((self._nowX)/self._nowSpX)
        else:
            if self._nowX < MAXX/2:
                #right
                xtime = abs(float((self._nowX)/self._nowSpX))
            else:
                #left
                xtime = abs(float((MAXX - self._nowX)/self._nowSpX))
        if self._nowSpY < 0:
            if self._nowY < MAXY/2:
                ytime = float((MAXY - self._nowY)/self._nowSpY)
            else:
                ytime = float((self._nowY)/self._nowSpY)
        else:
            if self._nowY < MAXY/2:
                ytime = abs(float((self._nowY)/self._nowSpY))
            else:
                ytime = abs(float((MAXY - self._nowY)/self._nowSpY))
        #need check ball touch time
        self.prints()
        #get next change time
        return min(xtime, ytime)

tb0 = ball(10, 10, 1, 2)
tb1 = ball(20, 20, 3, 4)
tb2 = ball(30, 30, 5, 6)
tb3 = ball(40, 40, 7, 8)
tb4 = ball(50, 50, 9, 10)
tb5 = ball(60, 60, -11, -12)
tb6 = ball(70, 70, -13, -14)
tb7 = ball(80, 80, -15, -16)
tb8 = ball(90, 90, -17, -18)

for i in range(1, 18, 2):
    tmp_obj = None
    if i < 10:
        tmp_obj = ball(i*10, i*10, i, i+1)
    else:
        tmp_obj = ball(i*10, i*10, i*(-1), (i+1) * (-1))
    listArr.append(tmp_obj)

c = 0
for obj in listArr:
    if c > 5:
        print obj.countEnd(obj.getNextChangeTime())
        break
    c += 1

exit(0)
tb2 = ball(80,80, -15,-16)
print tb2.getNextChangeTime()
print tb2._spSQ
