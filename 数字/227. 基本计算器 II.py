#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/3/11 8:38 下午
@Author:  pulinghao
@File: 227. 基本计算器 II.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = num * 10 + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(-int(abs(top) // num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)


if __name__ == '__main__':
    out = Solution().calculate(s = "14-3/2")

    print out
