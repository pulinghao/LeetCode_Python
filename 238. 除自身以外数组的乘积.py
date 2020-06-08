#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/4 10:31 上午
@Author:  pulinghao
@File: 238. 除自身以外数组的乘积.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 左侧之积 * 右侧之积
        L = [0] * len(nums)
        R = [0] * len(nums)
        L[0] = 1 # 左侧第一个元素为1
        R[-1] = 1 # 右侧第一个元素为1
        res = []
        N = len(nums)
        for i in range(1,len(nums)):
            L[i] = L[i - 1] * nums[i - 1]

        for i in range(N - 2, -1 , -1):
            R[i] = R[i + 1] * nums[i + 1]

        for i in range(N):
            res.append(L[i] * R[i])
        return res

if __name__ == '__main__':
    line = "[]"


    out = Solution().productExceptSelf(nums = [1,2,3,4])

    print out 