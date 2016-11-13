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


def heapify(array, i, n):
    j = i * 2 + 1
    while j < n:
        if j + 1 < n and compare(array[j].id, array[j+1].id):
            j += 1
        if not compare(array[i].id, array[j].id):
            break
        array[i], array[j] = array[j], array[i]
        i = j
        j = i * 2 + 1


def build_heap(array):
    size = len(array)
    for i in range( size // 2 - 1, -1, -1):
        heapify( array, i, size)


def heap_sort(array):
    size = len(array)
    build_heap(array)
    for i in range( size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)


# def heapify( array, i, n):
#     j = i * 2 + 1
#     while j < n:
#         #if j + 1 < n and compare(array[j].id, array[j+1].id):
#         if j + 1 < n and array[j] < array[j + 1]:
#             j += 1
#         #if not compare(array[i].id, array[j].id):
#         if array[i] > array[j]:
#             break
#         array[i], array[j] = array[j], array[i]
#         i = j
#         j = i * 2 + 1


def fixDown(a, k, n):  # 自顶向下堆化，从k开始堆化
    N = n - 1
    while 2 * k <= N:
        j = 2*k
        if j < N and compare(a[j].id, a[j+1].id):
            j += 1
        if compare(a[k].id, a[j].id):
            a[k], a[j] = a[j], a[k]
            k = j
        else:
            break


def heapSort(l):
    n = len(l) - 1
    for i in range(n//2, 0, -1):
        fixDown(l, i, len(l))
    while n > 1:
        l[1], l[n] = l[n], l[1]
        fixDown(l, 1, n)
        n -= 1
    res = l[1:]
    #res.append(l[0])
    return res


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
        self.heap_sort(items)
        return items

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

    def heapify(self, array, i, n):
        j = i * 2 + 1
        while j < n:
            if j + 1 < n and self.compare(array[j].id, array[j+1].id):
                j += 1
            if not self.compare(array[i].id, array[j].id):
                break
            array[i], array[j] = array[j], array[i]
            i = j
            j = i * 2 + 1

    def build_heap(self, array):
        size = len(array)
        for i in range(size // 2 - 1, -1, -1):
            self.heapify( array, i, size)

    def heap_sort(self, array):
        size = len(array)
        self.build_heap(array)
        for i in range( size - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            self.heapify(array, 0, i)


class Item:
    def __init__(self, id, position):
        self.id = id
        self.position = position

if __name__ == '__main__':
    # tt = [45,3,44,2,99]
    # heap_sort(tt)
    # print tt
    # print heapSort(tt)
    # quick_sort(tt, 0, len(tt)-1)
    # print tt[::-1]
    #exit(0)
    ll = []
    for i in xrange(11, 100):
        ll.append(Item(i, i))
    a = Item(10, 2)
    b = Item(2, 3)
    c = Item(5, 7)
    d = Item(1, 33)
    ll.append(a)
    ll.append(b)
    ll.append(c)
    ll.append(d)
    #tt = heapSort(ll)
    # heap_sort(ll)
    # for nl in ll:
    #     print nl.id
    # exit(0)
    ans = Answer()
 #   print ans.shellSort(ll)
    print "=======end==========="
    for a in ans.solve(ll):
        print a.id
    # print "================"
    # print mergesort(ll)
