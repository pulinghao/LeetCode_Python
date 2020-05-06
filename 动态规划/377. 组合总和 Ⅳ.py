#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/1 3:54 下午
 @Author   :pulinghao@baidu.com
 @File     :377. 组合总和 Ⅳ.py 
 @Description :
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        # 完全背包问题 ，可以有重复解，顺序可以变
        length = target
        dp = [0] * (target + 1)

        # 不放东西，也算一种
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] = dp[i] + dp[i - num]

        return dp[length]


if __name__ == '__main__':
    print Solution().combinationSum4(nums = [1,2,3],target = 4)