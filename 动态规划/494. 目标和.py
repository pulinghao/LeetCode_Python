#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/1 4:00 下午
 @Author   :pulinghao@baidu.com
 @File     :494. 目标和.py 
 @Description :
"""


class Solution(object):


    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        #dp = [[0] * 2001] * len(nums)  # 二维数组不能这么初始化，会出现浅拷贝的问题
        dp  = [[0 for i in range(2001)] for i in range(len(nums))]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            for x in range(-1000, 1001):
                if dp[i - 1][x + 1000] > 0:  # dp表示方案数，必须大于0
                    dp[i][x + 1000 + nums[i]] += dp[i - 1][x + 1000]
                    dp[i][x + 1000 - nums[i]] += dp[i - 1][x + 1000]

        return 0 if S > 1000 else dp[len(nums) - 1][S + 1000]



if __name__ == '__main__':
    print Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], S=3)
