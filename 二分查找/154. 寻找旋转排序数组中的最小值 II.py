#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/4/9 2:32 下午
@Author:  pulinghao
@File: 154. 寻找旋转排序数组中的最小值 II.py
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
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            else:
                mid = left + (right - left) // 2
                while mid + 1 < len(nums) and [mid] == nums[mid + 1]:
                    mid += 1

                if nums[mid + 1] >= nums[mid]:
                    left = mid + 1
                elif nums[mid + 1] < nums[mid]:
                    return nums[mid + 1]

        return nums[right]

        pass

if __name__ == '__main__':
    nums =[3,1,3]
    out = Solution().findMin(nums)

    print out
