#!/usr/bin/env python
#coding=utf-8

#rf.data url:http://www.qlcoder.com/download/rf.data
f = file('rf.data', 'rb')

filename = 1
signal = 0
while True:
    #signal = int.from_bytes(f.read(1), byteorder='big')
    signal = int(f.read(1).encode('hex'), 16)
    if signal == 2:
        break
    else:
        #size = int.from_bytes(f.read(4), byteorder='big')
        size = int(f.read(4).encode('hex'), 16)
        content = f.read(size)
        if signal == 0:
            with open(str(filename)+'.png', 'wb') as fout:
                fout.write(content)
            filename += 1
f.close()

