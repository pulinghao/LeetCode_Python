#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/14 10:59 下午
 @Author   :pulinghao@baidu.com
 @File     :188. 买卖股票的最佳时机 IV.py 
 @Description :
"""


class Solution(object):

    def other_may(self, k ,prices):

        if not prices or not k:
            return 0
        n = len(prices)

        # 当k大于数组长度的一半时，等同于不限次数交易即122题，用贪心算法解决，否则LeetCode会超时，也可以直接把超大的k替换为数组的一半，就不用写额外的贪心算法函数
        if k > len(prices) // 2:
            return self.greedy(prices)

        dp, res = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)], []
        # dp[i][k][0]表示第i天已交易k次时不持有股票 dp[i][k][1]表示第i天已交易k次时持有股票
        # 设定在卖出时加1次交易次数
        for i in range(k + 1):
            dp[0][i][0], dp[0][i][1] = 0, - prices[0]
        for i in range(1, n):
            for j in range(k + 1):
                if not j:
                    dp[i][j][0] = dp[i - 1][j][0]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])
        # 「所有交易次数最后一天不持有股票」的集合的最大值即为问题的解
        for m in range(k + 1):
            res.append(dp[n - 1][m][0])
        return max(res)

    # 处理k过大导致超时的问题，用贪心解决
    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        if k < 1:
            return 0

        def maxProfitWithInfinity(prices):
            dp = [[0 for _ in range(2)] for _ in range(len(prices))]
            dp[0][0] = 0
            dp[0][1] = -prices[0]

            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

            return dp[-1][0]

        # n = len(prices)
        # if n == 10:
        #     return maxProfitWithInfinity(prices)
        if k > len(prices) // 2:
            return maxProfitWithInfinity(prices)
        else:
            dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(len(prices))]
            for i in range(0, len(prices)):
                # 这里对 交易笔数进行了全部列举
                for j in range(k, 0, -1):
                    if i == 0:
                        dp[0][j][0] = 0
                        dp[0][j][1] = -prices[0]
                        continue
                    # dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i]);
                    # dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i]);
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

            return dp[-1][k][0]


if __name__ == '__main__':
    print Solution().maxProfit(2,[3,3,5,0,0,3,1,4])