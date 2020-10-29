#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/26 10:50 上午
@Author:  pulinghao
@File: 1365. 有多少小于当前数字的数字.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    cnt += 1

            res[i] = cnt
        return res

if __name__ == '__main__':
    nums = [8,1,2,2,3]

    out = Solution().smallerNumbersThanCurrent(nums)

    print out
