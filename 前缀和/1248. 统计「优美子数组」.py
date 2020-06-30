#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/29 5:12 下午
@Author:  pulinghao
@File: 1248. 统计「优美子数组」.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        前缀和
        """

        mp = [0] * (len(nums) + 1) # 下标表示 有多少个奇数 ， 值表示满足这个条件的子数组个数
        sum = 0 # 计数的个数
        mp[0] = 1
        res = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                sum += 1
            # 不管是不是奇数，都要增加1
            mp[sum] += 1
            if sum >= k:
                res += mp[sum - k]

        return res
        pass

if __name__ == '__main__':
    out = Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)

    print out 