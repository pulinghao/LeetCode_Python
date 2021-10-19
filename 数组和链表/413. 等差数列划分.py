#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/3/24 8:48 下午
@Author:  pulinghao
@File: 413. 等差数列划分.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        if n < 3:
            return res

        d = nums[1] - nums[0]
        cnt = 0
        for i in range(2,len(nums)):
            if nums[i] - nums[i - 1] == d:
                cnt += 1
                res += cnt
            else:
                d = nums[i] - nums[i - 1]
                cnt = 0

        return res
if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().func(root)

    print out
