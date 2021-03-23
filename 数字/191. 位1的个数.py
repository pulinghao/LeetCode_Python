#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/3/22 9:40 上午
@Author:  pulinghao
@File: 191. 位1的个数.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret

if __name__ == '__main__':
    x = 11
    s = bin(x)
    n = int(bin(x)[2:])
    out = Solution().hammingWeight(n)

    print out
