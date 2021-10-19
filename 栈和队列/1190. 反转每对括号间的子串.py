#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/5/26 5:30 下午
@Author:  pulinghao
@File: 1190. 反转每对括号间的子串.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                for t in temp:
                    stack.append(t)

        return ''.join(stack)



if __name__ == '__main__':
    s = ""
    out = Solution().reverseParentheses(s)

    print out
