#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/9 12:11 下午
@Author:  pulinghao
@File: 面试题 17.13. 恢复空格.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        dp = [0] * (len(sentence) + 1)
        dp[0] = 0
        setDict = set(dictionary)
        for i in range(1,len(sentence) + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 1, -1, -1):
                word = sentence[j:i]
                if word in setDict:
                    dp[i] = min(dp[i],dp[j])
                else:
                    dp[i] = min(dp[i],dp[j] + i - j)

        return dp[-1]




if __name__ == '__main__':
    dictionary = ["looked","just","like","her","brother"]
    sentence = "jesslookedjustliketimherbrother"
    out = Solution().respace(dictionary,sentence)

    print out 