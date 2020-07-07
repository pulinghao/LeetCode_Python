#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/4 12:24 上午
 @Author   :pulinghao@baidu.com
 @File     :32. 最长有效括号.py 
 @Description : 动态规划
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif dp[i - 1] > 0:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + 2
                        if i - dp[i - 1] - 2 >= 0:
                            dp[i] = dp[i] + dp[i - dp[i - 1] - 2]
                res = max(res, dp[i])

        return res


if __name__ == '__main__':
    print Solution().longestValidParentheses(s="()(())")
