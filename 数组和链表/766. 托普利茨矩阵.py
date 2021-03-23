#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/2/22 6:26 下午
@Author:  pulinghao
@File: 766. 托普利茨矩阵.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M = len(matrix)
        N = len(matrix[0])
        K = M + N - 1
        for i in range(K):
            if i < M:
                x = M - i - 1
                y = 0
            else:
                x = 0
                y = i - M + 1
            first = matrix[x][y]
            while x < M and y < N:
                if matrix[x][y] == first:
                    x += 1
                    y += 1
                else:
                    return False

        return True



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    matrix = [[1, 2], [2, 2]]
    out = Solution().isToeplitzMatrix(matrix)

    print out
