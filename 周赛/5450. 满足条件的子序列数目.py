#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/28 12:19 下午
 @Author   :pulinghao@baidu.com
 @File     :5450. 满足条件的子序列数目.py 
 @Description :
"""

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        数学问题
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        res = 0
        if nums[0] * 2 > target:
            return 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                # left 和 right中间有 N个数，那么有 2^N个排列组合（相当于是N个位置，每
                # 个位置的数字，有放和不放，两个可能)
                res += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return res%(10**9+7)

if __name__ == '__main__':
    print Solution().numSubseq(nums = [3,3,6,8], target = 10)