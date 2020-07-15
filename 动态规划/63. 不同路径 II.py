#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/6 10:51 上午
@Author:  pulinghao
@File: 63. 不同路径 II.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        N = len(obstacleGrid)  # N行
        M = len(obstacleGrid[0])  # M列
        dp = [[0 for _ in range(M)] for _ in range(N)]

        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0
        else:
            dp[0][0] = 1

        for i in range(1, N):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i - 1][0]

        for j in range(1, M):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, N):
            for j in range(1, M):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    M = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    out = Solution().uniquePathsWithObstacles(M)

    print out
