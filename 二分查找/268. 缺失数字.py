#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/26 7:27 下午
@Author:  pulinghao
@File: 268. 缺失数字.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1.先求和
        sumValue = len(nums) * (len(nums) + 1) / 2

        # 2.再将和减去每个数
        for num in nums:
            sumValue = sumValue - num
        return sumValue

    # 位运算方法

    def missingNumberByBit(self, nums):
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]

        return missing

if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().missingNumberByBit( [9,6,4,2,3,5,7,0,1])

    print out 