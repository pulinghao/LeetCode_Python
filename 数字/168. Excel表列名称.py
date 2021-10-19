#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/6/29 17:02
@Author:  pulinghao
@File: 168. Excel表列名称.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = list()
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(ans[::-1])


if __name__ == '__main__':

