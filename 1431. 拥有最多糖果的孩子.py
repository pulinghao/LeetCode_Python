#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/1 11:11 上午
@Author:  pulinghao
@File: 1431. 拥有最多糖果的孩子.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandy = max(candies)

        res = []
        for candy in candies:
            if candy + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res

        pass
if __name__ == '__main__':

    out = Solution().kidsWithCandies(candies = [12,1,12], extraCandies = 10)

    print out 