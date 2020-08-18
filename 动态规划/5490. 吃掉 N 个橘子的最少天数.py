#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/16 11:20 下午
 @Author   :pulinghao@baidu.com
 @File     :5490. 吃掉 N 个橘子的最少天数.py 
 @Description :
"""

import backports.functools_lru_cache

class Solution(object):
    def __init__(self):
        self.map = {}
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.map.keys():
            return self.map[n]

        if n == 0:
            self.map[n] = 0
            return 0

        if n == 1:
            self.map[n] = 1
            return 1

        # 每天吃一个桔子的方式，肯定比后面两个方案要慢
        #res = self.minDays(n - 1) + 1

        self.map[n] = 1 + min(self.minDays(n/2) + n % 2,self.minDays(n/3) + n % 3)

        return 1 + min(self.minDays(n/2) + n % 2,self.minDays(n/3) + n % 3)
        pass

if __name__ == '__main__':
    print Solution().minDays(n = 6)