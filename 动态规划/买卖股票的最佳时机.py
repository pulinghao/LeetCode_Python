#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/11 6:33 下午
@Author:  pulinghao
@File: 买卖股票的最佳时机.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        m = 2 # 两个状态，持有或者不持有股票
        n = 1 # 最多交易数
        l = len(prices)
        dp = [[[0 for i in range(m)] for i in range(n + 1)] for i in range(l)]

        for i in range(l):
            for j in range(1, 2):
                # 第i天持有不持有股票的最大利润
                if i - 1 == -1:
                    dp[i][0][0] = 0
                    dp[i][0][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0],dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i],dp[i - 1][j][1])  # j-1 把buy作为一次交易

        return dp[-1][n][0]


if __name__ == '__main__':
    print Solution().maxProfit(prices=[7,1,5,3,6,4])