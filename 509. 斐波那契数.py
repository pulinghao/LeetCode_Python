#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/4 9:37 下午
 @Author  :pulinghao@baidu.com
 @File     :509. 斐波那契数.py
 @Description :
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        if n == 1:
            return 1

        f = [0] * (n + 1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]

if __name__ == '__main__':
    n = 30
    print Solution().fib(n)