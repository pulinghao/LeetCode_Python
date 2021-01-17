#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/10 10:38 下午
 @Author  :pulinghao@baidu.com
 @File     :228. 汇总区间.py
 @Description :
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if len(nums) == 0:
            return res

        start = 0
        i = 1
        while i < len(nums):
            while i < len(nums) and nums[i] - nums[i - 1] == 1:
                i += 1
            end = i - 1
            if start != end:
                res.append("\"" + str(nums[start]) + "->" + str(nums[end]) + "\"")
            else:
                res.append("\"" + str(nums[end]) + "\"")
            start = i
            i += 1

        if start == len(nums) - 1:
            res.append("\"" + str(nums[start]) + "\"")
        return res

if __name__ == '__main__':
    nums = [0,2,3,4,6,8,9]
    print Solution().summaryRanges(nums)