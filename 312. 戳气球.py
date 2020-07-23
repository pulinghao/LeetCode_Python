#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/19 11:14 下午
 @Author   :pulinghao@baidu.com
 @File     :312. 戳气球.py 
 @Description :
"""

from functools import lru_cache

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        vals = [1] + nums + [1]

        @lru_cache(None)
        def solve(left, right):
            if left >= right - 1:
                return 0
            best = 0
            for i in range(left + 1, right):
                total = vals[left] * vals[i] * vals[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)

            return best

        return solve(0, N + 1)


if __name__ == '__main__':
    print Solution().maxCoins([3, 1, 5, 8])
