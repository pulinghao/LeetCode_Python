#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/4 11:42 下午
 @Author  :pulinghao@baidu.com
 @File     :643. 子数组最大平均数 I.py
 @Description :
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        addRes = sum(nums[:k])
        for i in range(len(nums) - k + 1):
            addRes = max(sum(nums[i:i + k]), addRes)

        return addRes * 1.0 / k

if __name__ == '__main__':
    nums = [0,1,1,3,3]
    k = 4
    print Solution().findMaxAverage(nums,k)