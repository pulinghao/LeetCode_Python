#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/26 9:29 下午
 @Author   :pulinghao@baidu.com
 @File     :329. 矩阵中的最长递增路径.py 
 @Description :
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        N = len(matrix)
        M = len(matrix[0])
        memo = [[0 for _ in range(M)] for _ in range(N)]
        ans = 0
        for i in range(N):
            for j in range(M):
                ans = max(ans, self.dfs(matrix, i, j, memo))

        return ans

    def dfs(self, matrix, row, col, memo):
        if memo[row][col] != 0:
            return memo[row][col]

        memo[row][col] = 1  # 这里表示已经访问过了
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        N = len(matrix)
        M = len(matrix[0])
        for i in range(4):
            newRow = dir[i][0] + row
            newCol = dir[i][1] + col
            if 0 <= newCol and newCol < M and newRow >= 0 and newRow < N and matrix[newRow][newCol] < matrix[row][col]:
                memo[row][col] = max(memo[row][col], self.dfs(matrix, newRow, newCol, memo) + 1)

        return memo[row][col]


if __name__ == '__main__':
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    print Solution().longestIncreasingPath(matrix)
