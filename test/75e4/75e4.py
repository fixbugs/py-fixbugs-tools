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

    def getNextChangeTime(self):
        xtime = 0
        ytime = 0
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
        if self._nowSpY > 0:
            if self._nowY < MAXY/2:
                ytime = float((MAXY - self._nowY)/self._nowSpY)
            else:
                ytime = float((self._nowY)/self._nowSpY)
        else:
            if self._nowY < MAXY/2:
                ytime = abs(float((self._nowY)/self._nowSpY))
            else:
                ytime = abs(float((MAXY - self._nowY)/self._nowSpY))
        print xtime, ytime
        #get next change time
        return min(xtime, ytime)

tb = ball(10,10, 1,2)
nt1 = tb.getNextChangeTime()
print tb.countEnd(nt1)
print tb._nowX
print tb._nowY
print tb._spSQ

print "============="

tb2 = ball(80,80, -15,-16)
print tb2.getNextChangeTime()
print tb2._spSQ
