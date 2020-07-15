#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/8 1:04 下午
@Author:  pulinghao
@File: 162. 寻找峰值.py
@Software: PyCharm
"""

import leetcode_utils
import sys

class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1

        return l


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().findPeakElement(nums=[1,2,1,3,5,6,4])

    print out 