#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/23 10:12 下午
 @Author   :pulinghao@baidu.com
 @File     :面试题 08.11. 硬币.py 
 @Description :
"""

class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        coins = [1,5,10,25]
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        # 1. 必须按照coin进行排序，否则的话会有重复的问题
        # 比如说,n = 6这种情况，i从0开始是话， 势必会有重复情况
        for coin in coins:
            for i in range(coin, n + 1):
                dp[i] = (dp[i] + dp[i - coin])

        return dp[n] % 1000000007





if __name__ == '__main__':
    print Solution().waysToChange(n = 6)