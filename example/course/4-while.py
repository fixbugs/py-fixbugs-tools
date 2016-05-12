#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

birth = input('birth: ')
while birth:
    if birth <= 2016 and birth >= 1990:
        print('right')
        break
    else:
        birth = input('input birth again:')

