#!/usr/bin/env python
#coding=utf8
from PIL import Image
import imagehash
hash = imagehash.average_hash(Image.open('lenna.png'))
print hash
