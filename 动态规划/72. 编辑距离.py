#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/2 5:11 下午
 @Author   :pulinghao@baidu.com
 @File     :72. 编辑距离.py 
 @Description :
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # 这里 -1 是表示第i个字符
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

        return dp[m][n]


if __name__ == '__main__':
    print Solution().minDistance(word1="horse", word2="ros")
