#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/20 3:52 下午
 @Author   :pulinghao@baidu.com
 @File     :10. 正则表达式匹配.py 
 @Description :
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        return self.dpIsMatch(s, p)

    def dpIsMatch(self, s, p):
        n = len(p)
        m = len(s)
        # dp p中的前j个，和s中的前i个
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True
        for i in range(n):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(0, m):
            for j in range(0, n):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        # 匹配 0 次
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] or dp[i][j + 1] or dp[i + 1][j - 1]

        return dp[-1][-1]

    def recursiveIsMatch(self, s, p):
        """
        递归解法
        :param s:待匹配的字符
        :param p:
        :return:
        """

        if len(p) == 0:
            return len(s) == 0

        first_match = bool(s) and p[0] in {s[0], '.'}

        # 如果第二格字符是 *
        if len(p) > 1 and p[1] == '*':
            return (self.recursiveIsMatch(s, p[2:])) or first_match and self.recursiveIsMatch(s[1:], p)
            pass
        else:
            return first_match and self.recursiveIsMatch(s[1:], p[1:])


if __name__ == '__main__':
    print Solution().isMatch(s="aaa", p="aaaa")
