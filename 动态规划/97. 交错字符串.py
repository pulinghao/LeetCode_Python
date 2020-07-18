#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/18 11:46 上午
@Author:  pulinghao
@File: 97. 交错字符串.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        M = len(s2)
        N = len(s1)

        if len(s3) != M + N:
            return False
        dp = [[False for _ in range(M + 1)] for _ in range(N + 1)]

        dp[0][0] = True
        for i in range(1, M + 1):
            if s2[i - 1] == s3[i - 1]:
                dp[0][i] = dp[0][i - 1]
            else:
                break

        for i in range(1 , N + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]
            else:
                break

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                up = False  # 从上往下
                if s3[i + j - 1] == s1[i - 1]:
                    up = dp[i - 1][j]

                left = False # 从左往右
                if s3[i + j - 1] == s2[j - 1]:
                    left = dp[i][j - 1]

                dp[i][j] = up or left

        return dp[-1][-1]



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")

    print out
