#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/12/23 11:58 上午
@Author:  pulinghao
@File: 387. 字符串中的第一个唯一字符.py
@Software: PyCharm
"""

import leetcode_utils
import collections


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = collections.defaultdict(list)
        for i in range(len(s)):
            if s[i] in stack.keys():
                array = stack[s[i]]
                array[1] += 1
            else:
                stack[s[i]] = [i, 1]

        maxIdx = len(s)
        for k, v in stack.items():
            if v[1] == 1:
                if v[0] < maxIdx:
                    maxIdx = v[0]

        if maxIdx == len(s):
            return -1
        else:
            return maxIdx


if __name__ == '__main__':
    s = "aadadaad"
    out = Solution().firstUniqChar(s)
    print out
