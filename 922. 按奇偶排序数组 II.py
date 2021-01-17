#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/11/12 7:21 下午
 @Author  :pulinghao@baidu.com
 @File     :922. 按奇偶排序数组 II.py
 @Description :
"""


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(A) - 1

        while left < len(A) and right >= 0:
            while left < len(A) and A[left] % 2 == 0:
                left += 2

            while right >= 0 and A[right] % 2 == 1:
                right -= 2

            if left < len(A) and right >= 0:
                A[left], A[right] = A[right], A[left]
                left += 2
                right -= 2

        return A

if __name__ == '__main__':
    A = [3,2]
    print Solution().sortArrayByParityII(A)