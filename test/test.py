#!/usr/bin/env python


def get_data(num=2333):
    count = 0
    for i in range(2, 10000):
        if i % 2 == 0 or i % 3 == 0:
            count += 1
        if count == num:
            return i
    return False

print get_data()
