#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/11/3 10:17 上午
@Author:  pulinghao
@File: 941. 有效的山脉数组.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        left = 0
        right = len(A) - 1

        while left < len(A) - 1 and A[left] < A[left + 1]:
            left += 1

        while right > 0 and A[right] < A[right - 1]:
            right -= 1

        return left > 0 and right < len(A) - 1 and left == right


if __name__ == '__main__':
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    out = Solution().validMountainArray(A)

    print out
