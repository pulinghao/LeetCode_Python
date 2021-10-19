#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/5/27 9:30 上午
@Author:  pulinghao
@File: 461. 汉明距离.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        嗯嗯return bin(x ^ y).count("1")


if __name__ == '__main__':
    x = 1
    y = 4
    out = Solution().hammingDistance(x, y)

    print out
