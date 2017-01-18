#!/usr/bin/env python
#coding=utf8


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slen = len(s)
        lastList = list()
        nowList = list()
        for ns in range(0, slen):
            if s[ns] not in nowList:
                nowList.append(s[ns])
            else:
                llen = len(lastList)
                if len(nowList) >= llen:
                    lastList = list()
                    lastList = nowList
                nowList = list()
                nowList.append(s[ns])
        if len(nowList) >= len(lastList):
            lastList = nowList
        return len(lastList)

if __name__ == "__main__":
    a = Solution()
    s = "abcabcbb"
    st = "dvdw"
    #print a.lengthOfLongestSubstring(s)
    print a.lengthOfLongestSubstring(st)
