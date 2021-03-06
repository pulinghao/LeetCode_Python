#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/2 12:43 下午
@Author:  pulinghao
@File: 283. 移动零.py
@Software: PyCharm
"""
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # j指针保存非0的数字， 因为j比i小，肯定不会出现覆盖的情况
        # 如果j< length，那么就把剩下的位置用0补齐
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         j += 1
        #
        # while j < len(nums):
        #     nums[j] = 0
        #     j += 1
        #
        # return nums
        j = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
        return nums





if __name__ == '__main__':
    nums = [0,0,1]
    print Solution().moveZeroes(nums)