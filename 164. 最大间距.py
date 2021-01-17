#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/11/26 11:49 下午
 @Author  :pulinghao@baidu.com
 @File     :164. 最大间距.py
 @Description :
"""


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        nums.sort()
        res = 0
        for i in range(1,len(nums)):
            res = max(nums[i] - nums[i - 1], res)
        return res

if __name__ == '__main__':
    print Solution().maximumGap([3,6,9,1])