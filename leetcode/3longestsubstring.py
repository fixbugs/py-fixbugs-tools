#!/usr/bin/env python
#coding=utf8


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength

if __name__ == "__main__":
    a = Solution()
    s = "abcabcbb"
    st = "dvdwadfsafsdfd"
    #print a.lengthOfLongestSubstring(s)
    print a.lengthOfLongestSubstring(st)
