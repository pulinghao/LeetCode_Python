#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/13 2:06 下午
 @Author   :pulinghao@baidu.com
 @File     :309. 最佳买卖股票时机含冷冻期.py 
 @Description :
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        dp[1][0] = max(-prices[0] + prices[1],dp[0][0]) #max(dp[0][0],dp[0][1])
        dp[1][1] = max(-prices[1], - prices[0]) # 昨日持有，或者今日持有，取利益最大的

        for i in range(2 , len(prices)):
            dp[i][0] = max(dp[i - 1][0],dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1],dp[i - 2][0] - prices[i])

        return dp[-1][0]

if __name__ == '__main__':
    print Solution().maxProfit(prices=[1,2,3,0,2])