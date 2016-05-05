#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-


def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r


def bar():
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass


try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
    print('END')


try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
    print('END')


class FooError(ValueError):
        pass


def fooo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

fooo('0')
