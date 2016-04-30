#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-


def now():
    print '2016-04-30'

f = now

print now.__name__
print f.__name__


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print '2016-04-30'

print now()
#now = log(now)


#log more params
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2016-04-30')


print now()
# now = log('execute')(now)


import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
