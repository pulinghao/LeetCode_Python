#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/25 8:08 下午
@Author:  pulinghao
@File: 34. 在排序数组中查找元素的第一个和最后一个位置.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1.返回左边界
        def binarySearchLeft(nums,target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if left >= len(nums):
                return -1
            elif nums[left] != target:
                return -1

            return left

            pass

        # 2.返回右边界
        def binarySearchRight(nums,target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if right < 0:
                return -1
            elif nums[right] != target:
                return -1
            return right

            pass

        if len(nums) == 0:
            return [-1,-1]
        return [binarySearchLeft(nums,target),binarySearchRight(nums,target)]

if __name__ == '__main__':
    out = Solution().searchRange(nums=[2,2],target= 3)

    print out 