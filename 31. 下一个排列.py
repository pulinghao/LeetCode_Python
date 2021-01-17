#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/11/10 11:56 下午
 @Author  :pulinghao@baidu.com
 @File     :31. 下一个排列.py
 @Description :
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        j = len(nums) - 1
        k = len(nums) - 1
        while i >= 0 and j >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]

        temp = nums[j:]
        temp.sort()
        for i in range(j, len(nums)):
            nums[i] = temp[i - j]



if __name__ == '__main__':
    nums = [1, 3, 2]
    Solution().nextPermutation(nums)
    print nums
