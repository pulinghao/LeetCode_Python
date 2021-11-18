#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2021/11/7
 @Author   :pulinghao@baidu.com
 @File     :598. 范围求和 II
 @Description :
"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        mina, minb = m, n
        for a, b in ops:
            mina = min(mina, a)
            minb = min(minb, b)
        return mina * minb


if __name__ == '__main__':
    m = 3
    n = 3
    operations = [[2, 2], [3, 3]]
    print Solution().maxCount(m,n,operations)