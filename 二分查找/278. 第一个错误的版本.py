#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/26 8:11 下午
@Author:  pulinghao
@File: 278. 第一个错误的版本.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isBadVersion(version):
            if version >= 4:
                return True
            else:
                return False

        left = 1
        right = n

        while left < right:
            mid = left + (right - left) / 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right
        pass


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().firstBadVersion(n = 5)

    print out 