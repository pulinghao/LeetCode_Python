#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/5 10:35 下午
 @Author   :pulinghao@baidu.com
 @File     :44. 通配符匹配.py 
 @Description :
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.dp(s, p)

    def dp(self, s, p):
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] != '*':
                break
            dp[i][0] = True

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    s = "adceb"

    p = "*a*b"
    print Solution().isMatch(s, p)
