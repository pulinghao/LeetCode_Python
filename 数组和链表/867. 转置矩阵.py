#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/2/25 1:18 下午
@Author:  pulinghao
@File: 867. 转置矩阵.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(matrix)
        M = len(matrix[0])

        res = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(N):
            for j in range(M):
                res[j][i] = matrix[i][j]

        return res


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)
    matrix = [[1,2,3],[4,5,6]]
    out = Solution().transpose(matrix)

    print out
