#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

#birth = input('birth: ')
birth = raw_input('birth:')
print birth
exit(0)
while birth:
    if birth <= 2016 and birth >= 1990:
        print('right')
        break
    else:
        birth = input('input birth again:')

