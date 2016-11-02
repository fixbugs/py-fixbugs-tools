#!/usr/bin/env python
#coding=utf8

def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high].id >= key.id:
            high -= 1
        while low < high and array[high].id < key.id:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array, low, key_index)
        quick_sort(array, key_index+1, high)


def compare(a, b):
    if a>b:
        return False
    return True

def mergesort(seq):
      if len(seq)<=1:
          return seq
      mid = int(len(seq)/2)
      left = mergesort(seq[:mid])
      right = mergesort(seq[mid:])
      return merge(left,right)

def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if compare(left[i].id, right[j].id):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result


class Answer:
    def solve(self, items):
        size = len(items)
#        quick_sort(items,0,size-1)
#        return items
        newl = [0]*(size*5)
        for i in xrange(0, size):
            newl[int(items[i].id)] = items[i]
        res = list()
        for n in newl:
            if n != 0:
                res.append(n)
        return res
        #return mergesort(items)

class Item:
    def __init__(self, id, position):
        self.id = id
        self.position = position

if __name__ == '__main__':
    ll = []
    for i in xrange(5,10000):
        ll.append(Item(i,i))
    a = Item(10,2)
    b = Item(2,3)
    c = Item(5,7)
    ll.append(a)
    ll.append(b)
    ll.append(c)
    ans = Answer()
    print len(ll)
    print "=======end==========="
    print ans.solve(ll)
    # print "================"
    # print mergesort(ll)
