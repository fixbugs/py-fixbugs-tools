#!/usr/bin/env python
#coding=utf8


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newl = nums1
        newl.extend(nums2)
        newl.sort()
        if len(newl) == 2:
            return int(float(sum(newl))/len(newl))
        tl = newl[1: -1]
        if len(tl) >= 1:
            return float(float(sum(tl))/len(tl))
        return int(float(sum(newl))/len(newl))

if __name__ == "__main__":
    a = Solution()
    n1 = [1]
    n2 = [2]
    print a.findMedianSortedArrays(n1, n2)
