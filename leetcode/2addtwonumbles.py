#!/usr/bin/env python
#coding=utf8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next


def initList(data):
    head = ListNode(data[0])
    p = head
    for i in data[1:]:
        node = ListNode(i)
        p.next = node
        p = p.next
    last = head
    return last

if __name__ == "__main__":
    a = Solution()
    ListF = list()
    ListS = list()
    FArr = [2,4,3]
    SArr = [5,6,4]
    ListF = initList(FArr)
    tl = ListF
    # while tl:
    #     print tl.val
    #     if tl.next:
    #         tl = tl.next
    #     else:
    #         break
    ListS = initList(SArr)
    print a.addTwoNumbers(ListF, ListS).next.next.val
