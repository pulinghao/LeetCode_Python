#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/8 11:49 下午
 @Author   :pulinghao@baidu.com
 @File     :221. 最大正方形.py 
 @Description :
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        maxSide = 0 # 保存最长边
        dp = [[0 for i in range(cols + 1)] for i in range(rows + 1)]
        # dp[i + 1][j + 1] 表示i,j个的最长边
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1],dp[i + 1][j]) + 1
                    maxSide = max(maxSide,dp[i + 1][j + 1])

        return maxSide * maxSide


if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print  Solution().maximalSquare(matrix)

