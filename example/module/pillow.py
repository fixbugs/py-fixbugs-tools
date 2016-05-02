#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#pip install Pillow


from PIL import Image

im = Image.open('test.png')

print(im.format, im.size, im.mode)

im.thumbnail((200, 100))

im.save('thumb.jpg', 'JPEG')


#path test
import sys

print sys.path

sys.path.append('/Users/michael/my_py_scripts')

print sys.path
