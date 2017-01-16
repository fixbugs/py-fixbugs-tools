#!/usr/bin/env python
#coding=utf8



class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = list()
    #     for i in range(0,n):
    #         result.append(self.getNumStr(i))
    #     return result

    # def getNumStr(self, n):
        numArr = self.numDoublesToList(n, 26)
        print numArr
        resultStr = ''
        for num in numArr:
            resultStr = resultStr + chr(64+num)
        return resultStr

    def numDoublesToList(self, num, basen):
        if num < basen:
            return [num]
        else:
            dnum = num/basen
            nnum = num
            result = list()
            while nnum/basen:
                result.append(int(nnum/basen))
                nnum = nnum - int(nnum/basen) * basen
            tnum = num - dnum*basen
            #result = list()
            #result.append(dnum)
            result.extend(self.numDoublesToList(tnum, basen))
            return result


if __name__ == "__main__":
    a = Solution()
    n = 24568
    print a.convertToTitle(n)
