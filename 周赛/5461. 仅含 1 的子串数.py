#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/12 3:02 下午
@Author:  pulinghao
@File: 5461. 仅含 1 的子串数.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """

        subString = s.strip().split('0')
        mode = 10 ** 9 + 7
        res = 0
        for str in subString:
            length = len(str)
            if length == 0:
                continue
            cnt = (length + 1) * length / 2
            res += cnt

        return res % mode



if __name__ == '__main__':
    print Solution().numSub(s="111111")

