#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/3/2 11:31 上午
@Author:  pulinghao
@File: 304. 二维区域和检索 - 矩阵不可变.py
@Software: PyCharm
"""

import leetcode_utils

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            M, N = 0,0
        else:
            M, N = len(matrix), len(matrix[0])
        self.preSum = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                self.preSum[i + 1][j + 1] = self.preSum[i][j + 1] + self.preSum[i + 1][j] - \
                                            self.preSum[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row2 + 1][col1] - \
               self.preSum[row1][col2 + 1] + self.preSum[row1][col1]


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


if __name__ == '__main__':
    matrix = [[[]]]
    obj = NumMatrix(matrix)
    out = obj.sumRegion(0,0,1,1)
