#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/28 11:27 下午
 @Author   :pulinghao@baidu.com
 @File     :面试题 17.06. 2出现的次数.py 
 @Description :
"""


class Solution(object):
    def numberOf2sInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            dp[i] = dp[i - 1] + self.numsof2(i)
        return dp[n]

    def numsof2(self, n):
        count = 0
        while n:
            if n % 10 == 2:
                count += 1
            n = n / 10

        if n % 10 == 2:
            count += 1
        return count


if __name__ == '__main__':
    print Solution().numberOf2sInRange(n=559366752)
