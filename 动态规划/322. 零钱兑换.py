#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/26 10:59 下午
 @Author   :pulinghao@baidu.com
 @File     :322. 零钱兑换.py 
 @Description :
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin,amount + 1):
                dp[i] = min(dp[i],dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    print Solution().coinChange(coins=[1,2,5],amount=11)