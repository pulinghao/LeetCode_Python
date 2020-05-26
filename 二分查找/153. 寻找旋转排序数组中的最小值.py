#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/26 8:53 下午
@Author:  pulinghao
@File: 153. 寻找旋转排序数组中的最小值.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().findMin([1,2,3])

    print out 