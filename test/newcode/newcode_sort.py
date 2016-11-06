#!/usr/bin/env python
#coding=utf8

import sys
sys.setrecursionlimit(1000000)


def sub_sort(array, low, high):
    key = array[low]
    while low < high:
        tmp_com_ret = compare(array[high].id, key.id)
        while low < high and not tmp_com_ret:
            high -= 1
        while low < high and tmp_com_ret:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        quick_sort(array, low, key_index)
        quick_sort(array, key_index+1, high)


def compare(a, b):
    if a > b:
        return False
    return True


def mergesort(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq)/2)
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i].id, right[j].id):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def countingSort(alist, k):
    n = len(alist)
    b = [0 for i in xrange(n)]
    c = [0 for i in xrange(k+1)]
    for i in alist:
        c[i.id] += 1
    len_c = len(c)
    for i in xrange(1, len_c):
        c[i] = c[i-1] + c[i]
#        c[i]=c[i-1]+c[i]
    for i in alist:
        b[c[i.id]-1] = i
#       b[c[i]-1]=i
        c[i.id] -= 1
    return b


class Answer:
    def solve(self, items):
#        size = len(items)
        return countingSort(items, 1000)


class Item:
    def __init__(self, id, position):
        self.id = id
        self.position = position

if __name__ == '__main__':
    ll = []
    for i in xrange(11, 100):
        ll.append(Item(i, i))
    a = Item(10, 2)
    b = Item(2, 3)
    c = Item(5, 7)
    ll.append(a)
    ll.append(b)
    ll.append(c)
    ans = Answer()
    print len(ll)
    print "=======end==========="
    print ans.solve(ll)
    # print "================"
    # print mergesort(ll)
