#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/10 9:48 下午
 @Author   :pulinghao@baidu.com
 @File     :300. 最长上升子序列.py 
 @Description :
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

if __name__ == '__main__':
    print Solution().lengthOfLIS(nums = [10,9,2,5,3,4])