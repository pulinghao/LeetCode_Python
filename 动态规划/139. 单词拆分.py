#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/29 11:49 下午
 @Author   :pulinghao@baidu.com
 @File     :139. 单词拆分.py 
 @Description :
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 背包大小
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1,n + 1):
            for word in wordDict:
                word_len = len(word)
                if i >= word_len and s[i - word_len : i] == word:
                    dp[i] = dp[i] or dp[i - word_len]

        return dp[n]

if __name__ == '__main__':
    print Solution().wordBreak(s="leetcode",wordDict=["leet","code"])
