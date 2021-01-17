#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/8 3:30 下午
 @Author  :pulinghao@baidu.com
 @File     :189. 旋转数组.py
 @Description :
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


if __name__ == '__main__':
    nums = [-1, -100, 3, 99]
    k = 2
    Solution().rotate(nums, k)
    print nums
