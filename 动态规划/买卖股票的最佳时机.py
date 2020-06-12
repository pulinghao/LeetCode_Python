#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/11 6:33 下午
@Author:  pulinghao
@File: 买卖股票的最佳时机.py
@Software: PyCharm
"""

import leetcode_utils
import sys

class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def func1(self,prices):
        m = 2  # 两个状态，持有或者不持有股票
        n = 1  # 最多交易数
        l = len(prices)
        dp = [[[0 for i in range(m)] for i in range(n + 1)] for i in range(l)]

        for i in range(l):
            for j in range(1, 2):
                # 第i天持有不持有股票的最大利润
                if i - 1 == -1:
                    dp[i][j][0] = 0
                    # dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
                    # dp[i - 1][1][1] = dp[0][1][1] = 负无穷（未做任何投资，但持有股票）
                    # dp[i-1][0][0] = dp[0][0][0] = 0
                    # dp[i][j][1] = -prices[i]
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i], dp[i - 1][j][1])  # j-1 把buy作为一次交易

        return dp[-1][n][0]

    def func2(self,prices):
        m = 2  # 两个状态，持有或者不持有股票
        n = 1  # 最多交易数
        l = len(prices)
        dp = [[0 for i in range(m)] for  i in range(l)]

        for i in range(l):
            # 第i天持有不持有股票的最大利润
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 不交易也不持有（j，k=0),那么dp[i][0][0] = 0
            dp[i][1] = max(-prices[i], dp[i - 1][1])


        return dp[-1][0]



    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.func1(prices)






if __name__ == '__main__':
    print Solution().maxProfit(prices=[7,1,5,3,6,4])