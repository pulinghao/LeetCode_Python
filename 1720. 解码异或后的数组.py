#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/5/6 8:19 下午
@Author:  pulinghao
@File: 1720. 解码异或后的数组.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        for num in encoded:
            arr.append(arr[-1] ^ num)
        return arr

if __name__ == '__main__':
    encoded = [0,6]
    first = 5
    out = Solution().decode(encoded,first)

    print out
