#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/11 11:11 下午
 @Author   :pulinghao@baidu.com
 @File     :122. 买卖股票的最佳时机 II.py 
 @Description :
"""
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 2  # 两个状态，持有或者不持有股票
        # n = 1  # 最多交易数
        l = len(prices)
        dp = [[0 for i in range(m)] for i in range(l)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,l):
            # if i - 1 == -1:
            #     dp[i][0] = 0
            #     dp[i][1] = -prices[i]
            #     continue

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

if __name__ == '__main__':
    print Solution().maxProfit(prices=[1,2,3,4,5])