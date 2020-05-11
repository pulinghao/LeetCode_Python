#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/11 11:06 下午
 @Author   :pulinghao@baidu.com
 @File     :1143. 最长公共子序列.py 
 @Description :
"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


if __name__ == '__main__':
    print Solution().longestCommonSubsequence(text1="abcde", text2="ace")
