#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/13 1:41 下午
 @Author   :pulinghao@baidu.com
 @File     :714. 买卖股票的最佳时机含手续费.py 
 @Description :
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

        # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

if __name__ == '__main__':
    print Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2)
