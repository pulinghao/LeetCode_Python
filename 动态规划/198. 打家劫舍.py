#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/13 1:16 下午
@Author:  pulinghao
@File: 198. 打家劫舍.py
@Software: PyCharm
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        sum2 = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                sum2 += nums[i]
            else:
                sum1 += nums[i]

        return sum1 if sum1 > sum2 else sum2



if __name__ == '__main__':
    nums = [1,2,3,4]
    print Solution().rob(nums)