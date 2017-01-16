#!/usr/bin/env python
#coding=utf8



class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = n
        return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))
        print chr(64+1)
        numArr = self.numDoublesToList(n, 26)
        print numArr
        resultStr = ''
        for num in numArr:
            if num > 0:
                resultStr = resultStr + chr(64+num)
        return resultStr

    def numDoublesToList(self, num, basen):
        result = list()
        while True:
            num, remainder = divmod(num, basen+1)
            result.append(remainder)
            if num == 0:
                return result[::-1]
        #return result
        # if num < basen:
        #     return [num]
        # else:
        #     dnum = num/basen
        #     nnum = num
        #     result = list()
        #     while nnum/basen:
        #         result.append(int(nnum/basen))
        #         nnum = nnum - int(nnum/basen) * basen
        #     tnum = num - dnum*basen
        #     #result = list()
        #     #result.append(dnum)
        #     result.extend(self.numDoublesToList(tnum, basen))
        #     return result


if __name__ == "__main__":
    a = Solution()
    n = 26
    print a.convertToTitle(n)
