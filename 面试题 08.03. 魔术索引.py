#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/31 10:18 上午
@Author:  pulinghao
@File: 面试题 08.03. 魔术索引.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == i:
                return i

        return -1


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().findMagicIndex(nums = [1, 1, 1])

    print out 