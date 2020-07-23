#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/23 7:40 上午
 @Author   :pulinghao@baidu.com
 @File     :64. 最小路径和.py 
 @Description :
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        M = len(grid[0])

        if N == 0 or M == 0:
            return 0

        dp = [[0 for _ in range(M)] for _ in range(N)]

        dp[0][0] = grid[0][0]
        for i in range(1, M):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, N):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, N):
            for j in range(1, M):
                dp[i][j] = min(dp[i - 1][j] + grid[i][j],dp[i][j - 1] + grid[i][j])

        return dp[-1][-1]


if __name__ == '__main__':

    grid = [[]
]
    print Solution().minPathSum(grid)
