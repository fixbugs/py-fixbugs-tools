#!/usr/bin/env python
#coding=utf8


class Solution(object):
    def test(self):
        pass

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)


if __name__ == "__main__":
    a = Solution()
    s = 'njkjkjnjff'
    n = 3
    print a.convert(s, n)
