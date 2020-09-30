#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/4 1:45 下午
@Author:  pulinghao
@File: 202. 快乐数.py
@Software: PyCharm
"""

import leetcode_utils
import collections


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def squre(n):
            res = 0
            while n / 10:
                r = n % 10
                res += r ** 2
                n = n / 10

            res += (n % 10) ** 2
            return res

        ans = False
        dict = collections.defaultdict(int)
        while True:
            r = squre(n)
            if r == 1:
                ans = True
                break
            else:
                if r in dict.keys():
                    ans = False
                    break
                else:
                    dict[r] = 1
            n = r

        return ans



if __name__ == '__main__':
    out = Solution().isHappy(109)

    print out
