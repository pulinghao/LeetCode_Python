#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/3/9 7:26 下午
@Author:  pulinghao
@File: 1047. 删除字符串中的所有相邻重复项.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []

        for c in S:
            if len(stack) and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)

if __name__ == '__main__':
    s = "abbaca"
    out = Solution().removeDuplicates(s)

    print out
