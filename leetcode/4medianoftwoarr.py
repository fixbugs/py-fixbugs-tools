#!/usr/bin/env python
#coding=utf8


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
            if n == 0:
                raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
        # newl = nums1
        # newl.extend(nums2)
        # newl.sort()
        # if len(newl) == 2:
        #     return int(float(sum(newl))/len(newl))
        # tl = newl[1: -1]
        # if len(tl) >= 1:
        #     return float(float(sum(tl))/len(tl))
        # return int(float(sum(newl))/len(newl))

if __name__ == "__main__":
    a = Solution()
    n1 = [1]
    n2 = [2]
    print a.findMedianSortedArrays(n1, n2)
