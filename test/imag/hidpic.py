#!/usr/bin/env python
#coding=utf-8

from PIL import Image
import urllib
import io

file = open('lenna.png')
tmpIm = io.BytesIO(file.read())
im = Image.open(tmpIm)
im.load()
r, g, b = im.split()
out = r.point(lambda i: (i%2 == 0)*200)
out.show()
