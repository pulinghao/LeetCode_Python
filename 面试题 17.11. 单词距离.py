#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time:  23:31
# @Author:pulinghao
# @File：面试题 17.11. 单词距离.py
# @Software: PyCharm

import  leetcode_utils
class Solution(object):
    def findClosest(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = -1
        p2 = -1
        res = leetcode_utils.INT_MAX
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            elif words[i] == word2:
                p2 = i

            if p1 != -1 and p2 != -1:
                res = min(res, abs(p1 - p2))
        return res


