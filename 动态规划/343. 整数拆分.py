#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/6 10:52 下午
 @Author   :pulinghao@baidu.com
 @File     :343. 整数拆分.py 
 @Description :
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        # 前i个数的最大值
        dp[1] = 1

        for i in range(2, len(dp)):
            for j in range(1, i):
                # 继续 dp[i - j] 表示，继续拆分，得到的结果
                # (i - j)表示不拆分得到的结果
                dp[i] = max(dp[i - j] * j, (i - j) * j, dp[i])

        return dp[-1]

if __name__ == '__main__':
    print Solution().integerBreak(n=10)
