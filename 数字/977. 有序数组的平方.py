#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/16 10:58 上午
@Author:  pulinghao
@File: 977. 有序数组的平方.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        res = [0] * N
        i = 0
        j = N - 1
        idx = N - 1  # 必须从最大开始倒排，不能从最小开始，最小的不知道，在中间
        while i <= j:
            if A[i] * A[i] < A[j] * A[j]:
                res[idx] = A[j] * A[j]
                j -= 1
            else:
                res[idx] = A[i] * A[i]
                i += 1
            idx -= 1
        return res
if __name__ == '__main__':
    A = [-7,-3,2,3,11]
    out = Solution().sortedSquares(A)
    print out
