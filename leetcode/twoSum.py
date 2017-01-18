#!/usr/bin/env python
#coding=utf8


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        newNums = nums
        result = list()
        for i in range(len(newNums)):
            firstN = newNums[i]
            needNum = target - firstN
            if needNum == firstN:
                tNewNums = newNums[i+1:]
                if needNum in tNewNums:
                    result.append(i)
                    result.append(tNewNums.index(needNum)+i+1)
                    break
            else:
                if needNum in newNums:
                    result.append(i)
                    result.append(newNums.index(needNum))
                    break
        return result

if __name__ == "__main__":
    a = Solution()
    n = [0,3,2,4,0]
    t = 0
    print a.twoSum(n, t)
