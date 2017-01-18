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
        # slen = len(s)
        # lastList = list()
        # nowList = list()
        # for ns in range(0, slen):
        #     if s[ns] not in nowList:
        #         nowList.append(s[ns])
        #     else:
        #         llen = len(lastList)
        #         if len(nowList) >= llen:
        #             lastList = list()
        #             lastList = nowList
        #         nowList = list()
        #         nowList.append(s[ns])
        # if len(nowList) >= len(lastList):
        #     lastList = nowList
        # return len(lastList)

if __name__ == "__main__":
    a = Solution()
    s = "abcabcbb"
    st = "dvdwadfsafsdfd"
    #print a.lengthOfLongestSubstring(s)
    print a.lengthOfLongestSubstring(st)
