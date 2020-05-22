#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/14 9:08 下午
@Author:  pulinghao
@File: 583. 两个字符串的删除操作.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M = len(word1) + 1
        N = len(word2) + 1

        # 创建DP数组
        dp = [[0 for _ in range(M)] for _ in range(N)]
        dp[0][0] = 0
        for i in range(M):
            dp[0][i] = i
        for i in range(N):
            dp[i][0] = i

        for i in range(1,N):
            for j in range(1,M):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 2,dp[i - 1][j] + 1,dp[i][j - 1] + 1)

        return dp[-1][-1]



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().minDistance(word1="a",word2="ab")

    print out 