#!/usr/bin/env python
#coding=utf8

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
    size = len(ll)
    newl = [0]*(size*10+1)
    for i in range(size):
        newl[int(ll[i].id)] = ll[i]
        res = list()
        for n in newl:
            if n != 0 :
                res.append(n)
    print ll
    print res
    # print "================"
    # print mergesort(ll)
