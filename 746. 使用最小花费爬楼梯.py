#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/12/21 8:45 下午
 @Author  :pulinghao@baidu.com
 @File     :746. 使用最小花费爬楼梯.py
 @Description :
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost) + 1
        dp = [0] * N
        dp[0] = 0
        dp[1] = 0

        for i in range(2, N):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[-1]

if __name__ == '__main__':
    cost =   [10, 15, 20]
    print Solution().minCostClimbingStairs(cost)
