#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/27 11:19 下午
 @Author   :pulinghao@baidu.com
 @File     :518. 零钱兑换 II.py 
 @Description :
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i - coin]
        return dp[amount]

if __name__ == '__main__':
    print Solution().change(amount=3 ,coins = [2])