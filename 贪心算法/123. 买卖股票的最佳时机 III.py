#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/14 10:21 下午
 @Author   :pulinghao@baidu.com
 @File     :123. 买卖股票的最佳时机 III.py 
 @Description :
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]

        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]

        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]

        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]

        for i in range(1, len(prices)):
            # 这里对 交易笔数进行了全部列举
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])

            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
        return dp[-1][2][0]

if __name__ == '__main__':
    print Solution().maxProfit([3,3,5,0,0,3,1,4])