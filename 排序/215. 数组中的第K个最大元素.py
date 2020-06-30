#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/29 3:21 下午
@Author:  pulinghao
@File: 215. 数组中的第K个最大元素.py
@Software: PyCharm
"""

import leetcode_utils
import random

class Solution:
    def findKthLargest(self, nums, k):
        size = len(nums)

        target = size - k
        left = 0
        right = size - 1
        while True:
            index = self.partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                # 下一轮在 [index + 1, right] 里找
                left = index + 1
            else:
                right = index - 1

    #  循环不变量：[left + 1, j] < pivot
    #  (j, i) >= pivot
    def __partition(self, nums, left, right):
        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

    def partition(self,nums,left,right):
        index = random.randint(left,right)
        # index = 3
        # 交换到第一个位置
        nums[left],nums[index] = nums[index],nums[left]
        pivot = nums[left]
        l = left + 1
        r = right
        while l <= r:
            while l <= r and nums[l] <= pivot:
                l += 1

            while l <= r and nums[r] >= pivot:
                r -= 1

            if l <= r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        nums[left],nums[l - 1] = nums[l - 1],nums[left]
        px = l - 1
        return px


if __name__ == '__main__':
    out = Solution().findKthLargest([3,2,3,1,2,4,5,5,6] ,k = 4)
    # nums=[5,2,4,1,3,6,0]
    # out = Solution().partition(nums,left = 0 , right = len(nums) - 1)
    print out 