#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np


MAXX = 1000
MAXY = 1000

listArr = []


class ball(object):
    def __init__(self, initX, initY, spX, spY):
        self._nowX = initX
        self._nowY = initY
        self._nowSpX = spX
        self._nowSpY = spY

    def countEnd(self, timePass):
        self._nowX += timePass * self._nowSpX
        self._nowY += timePass * self._nowSpY

    def setNewSpeed(self, newX, newY):
        self._nowSpX = newX
        self._nowSpY = newY

    def getNextChangeTime():
        #get next change time
        pass
