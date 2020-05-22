#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/21 7:36 下午
@Author:  pulinghao
@File: 5. 最长回文子串.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        length = 1 # 最小长度为1，单个字符也是回文子串
        res = s[0:1]
        for i in range(n - 1, -1 , -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                else:
                    if j - i + 1 == 2:
                        if s[i] == s[j]:
                            dp[i][j] = True
                        else:
                            dp[i][j] = False
                    else:
                        dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

                if dp[i][j]:
                    if length < j - i + 1:
                        length = j - i + 1
                        res = s[i : j + 1]

        return res

if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().longestPalindrome(s="cbbd")

    print out 