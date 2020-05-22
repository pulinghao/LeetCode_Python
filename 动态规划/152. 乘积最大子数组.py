#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/18 8:04 下午
@Author:  pulinghao
@File: 152. 乘积最大子数组.py
@Software: PyCharm
"""

import leetcode_utils

import math
class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 1. 二维数组解法
        # 构造一个正数数组，一个负数数组
        # maxF = [0 for _ in range(len(nums))]
        # minF = [0 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     maxF[i] = nums[i]
        #     minF[i] = nums[i]
        #
        # for i in range(1,len(nums)):
        #     maxF[i] = max(maxF[i - 1] * nums[i], minF[i - 1] * nums[i], nums[i])
        #     minF[i] = min(maxF[i - 1] * nums[i], minF[i - 1] * nums[i], nums[i])
        #
        # return max(maxF)

        # 2.滚动数组，节省空间

        MF = nums[0]
        MI = nums[0]
        res = MF
        for i in range(1,len(nums)):
            # 这里需要把老的值保存一下，否则的话会出现覆盖的问题
            mf = MF
            mi = MI
            MF = max(mf * nums[i], mi * nums[i], nums[i])
            MI = min(mf * nums[i], mi * nums[i], nums[i])
            # MF = max(MF * nums[i], MI * nums[i], nums[i])
            # MI = min(MF * nums[i], MI * nums[i], nums[i])
            res = max(res,MF)
        return res



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().maxProduct(nums=[-4,-3,-2])

    print out 