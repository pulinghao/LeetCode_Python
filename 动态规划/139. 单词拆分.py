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

        for i in range(1, n + 1):
            for word in wordDict:
                word_len = len(word)
                if i >= word_len and s[i - word_len: i] == word:
                    dp[i] = dp[i] or dp[i - word_len]

        return dp[n]

    def dfs(self, s, wordDict):
        # dfs 方法
        # memo存储从start到s结尾时，是否是为True
        # 如果为True，就不需要把[start:s]的字符串进行拆分了
        memo = {}

        def check(s, wordSet, start):
            if start > len(s) - 1:
                return True

            if start in memo:
                return memo[start]
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and check(s, wordSet, end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return check(s, wordDict, 0)

        pass


if __name__ == '__main__':
    print Solution().dfs(s="leetcode", wordDict=["leet", "code"])
