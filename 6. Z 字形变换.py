#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/13 1:00 下午
@Author:  pulinghao
@File: 6. Z 字形变换.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        numslist = []
        for i in range(numRows):
            numslist.append([])

        modValue = numRows + (numRows - 2)
        for i in range(len(s)):
            rest = i % modValue
            if rest >= numRows:
                sublist = numslist[numRows - 1 - (rest - numRows + 1)]
                sublist.append(s[i])
            else:
                sublist = numslist[rest]
                sublist.append(s[i])
        res = ''
        for strlist in numslist:
            str = ''.join(strlist)
            res += str

        return res

if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().convert(s = "A", numRows = 1)

    print out 