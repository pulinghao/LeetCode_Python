#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time:  22:46
# @Author:pulinghao
# @File：剑指 Offer II 114. 外星文字典.py
# @Software: PyCharm

import  leetcode_utils

VISITINT = 1
VISITED = 2
edges = {}
valid = True


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        length = len(words)
        for word in words:
            for c in word:
                if c in edges.keys():
                    pass
                else:
                    edges[c] = []


