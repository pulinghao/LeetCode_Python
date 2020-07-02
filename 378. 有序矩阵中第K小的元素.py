#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/2 10:38 上午
@Author:  pulinghao
@File: 378. 有序矩阵中第K小的元素.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        N = len(matrix)

        r = k / N
        l = k % N
        if l != 0:
            l -= 1
        else:
            r -= 1
            l = N - 1
        return matrix[r][l]

if __name__ == '__main__':
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    k = 8
    out = Solution().kthSmallest(matrix,k)

    print out 