#!/usr/bin/env python
#coding=utf8

import sys
sys.setrecursionlimit(1000000)


# def sub_sort(array, low, high):
#     key = array[low]
#     while low < high:
#         tmp_com_ret = compare(array[high].id, key.id)
#         while low < high and tmp_com_ret:
#             high -= 1
#         tmp_com_ret = compare(array[high].id, key.id)
#         while low < high and not tmp_com_ret:
#             array[low] = array[high]
#             low += 1
#             array[high] = array[low]
#     array[low] = key
#     return low


# def quick_sort(array, low, high):
#     if low < high:
#         key_index = sub_sort(array, low, high)
#         quick_sort(array, low, key_index)
#         quick_sort(array, key_index+1, high)

def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        tmp_com_ret = compare(lists[high].id, key.id)
        while left < right and not tmp_com_ret:
            right -= 1
        lists[left] = lists[right]
        tmp_com_ret = compare(lists[high].id, key.id)
        while left < right and tmp_com_ret:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


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


class Answer():
    def solve(self, items):
        return self.spsort(items, 100)

    def shellSort(self, seq):
        count = len(seq)
        step = 2
        group = count/step
        while group > 0:
            for i in range(0, group):
                j = i + group
                while j < count:
                    k = j - group
                    key = seq[j]
                    while k >= 0:
                        if not self.compare(seq[k].id, key.id):
#                        if seq[k].id > key.id:
                            seq[k + group] = seq[k]
                            seq[k] = key
                        k -= group
                    j += group
            group /= step
        return seq

    def spsort(self, items, buckCount):
        buckList = list()
        for i in xrange(0, buckCount):
            tmp = list()
            buckList.append(tmp)
        total = 1000000
        perCount = total/buckCount
        for i in items:
            bnum = int(i.id/perCount)
            buckList[bnum].append(i)
        res = list()
        for b in buckList:
            if not b:
                continue
            res.extend(self.shellSort(b))
        return res

    def mergesort(self, seq):
        if len(seq) <= 1:
            return seq
        mid = int(len(seq)/2)
        left = self.mergesort(seq[:mid])
        right = self.mergesort(seq[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if self.compare(left[i].id, right[j].id):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def compare(self, a, b):
        if a > b:
            return False
        return True


class Item:
    def __init__(self, id, position):
        self.id = id
        self.position = position

if __name__ == '__main__':
    # tt = [45,3,44,2,99]
    # quick_sort(tt, 0, len(tt)-1)
    # print tt[::-1]
    # exit(0)
    ll = []
#    for i in xrange(11, 100):
#        ll.append(Item(i, i))
    a = Item(10, 2)
    b = Item(2, 3)
    c = Item(5, 7)
    d = Item(1,33)
    ll.append(a)
    ll.append(b)
    ll.append(c)
    ll.append(d)
    quick_sort(ll, 0, len(ll)-1)
    for nl in ll:
        print nl.id
    exit(0)
    ans = Answer()
 #   print ans.shellSort(ll)
    print "=======end==========="
    for a in ans.solve(ll):
        print a.id
    # print "================"
    # print mergesort(ll)
