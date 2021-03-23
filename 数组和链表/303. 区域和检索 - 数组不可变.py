#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/3/1 6:26 下午
@Author:  pulinghao
@File: 303. 区域和检索 - 数组不可变.py
@Software: PyCharm
"""

import leetcode_utils

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        import collections
        self.numDict = collections.defaultdict(int)
        self.numDict[-1] = 0
        for i in range(len(nums)):
            self.numDict[i] = self.numDict[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.numDict[j] - self.numDict[i - 1]


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    param_1 = obj.sumRange(2, 5)
    print param_1
