#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/11 11:07 上午
@Author:  pulinghao
@File: 739. 每日温度.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while len(stack) != 0 and T[i] > T[stack[-1]]:
                top = stack.pop(-1)
                ans[top] = i - top
                pass

            stack.append(i)  # 这里存的是索引，而不是数值
        return ans
if __name__ == '__main__':
    line = "[]"


    out = Solution().dailyTemperatures(T= [73, 74, 75, 71, 69, 72, 76, 73])

    print out 