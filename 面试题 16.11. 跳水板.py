#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/8 10:33 上午
@Author:  pulinghao
@File: 面试题 16.11. 跳水板.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        list = []
        for i in range(k + 1):
            length = i * longer + (k - i) * shorter
            list.append(length)
        return list

if __name__ == '__main__':
    out = Solution().divingBoard(shorter= 2 ,longer = 1118596 , k = 979)

    print out 