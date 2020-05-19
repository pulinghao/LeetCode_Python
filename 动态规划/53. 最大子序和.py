#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/18 11:18 下午
 @Author   :pulinghao@baidu.com
 @File     :53. 最大子序和.py 
 @Description :
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i],nums[i])
            res = max(dp[i],res)
        return res



if __name__ == '__main__':
    print Solution().maxSubArray(nums= [31,-41,59,26,-53,58,97,-93,-23,84])