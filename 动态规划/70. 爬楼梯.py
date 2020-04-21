#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/21 7:34 下午
@Author:  pulinghao
@File: 70. 爬楼梯.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 递归思路,结果超时
        if n == 1:
            return 1

        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # 保存值的方式
    def dpValue(self,n):
        if n == 1:
            return 1

        if n == 2:
            return 2

        cur = 2;
        pre = 1
        i = 3
        res = 0
        while i <= n:
            res = cur + pre
            pre = cur
            cur = res
            i += 1
        return res

    # 保存数组思路

    def dpArray(self,n):
        res = []
        i = 0
        while i <= n:
            if i == 0:
                res.append(0)
            elif i == 1:
                res.append(1)
            elif i == 2:
                res.append(2)
            else:
                ret = res[i - 1] + res[i - 2]
                res.append(ret)
            i += 1
        return res[-1]

if __name__ == '__main__':
    n = 10
    print Solution().dpArray(n)
    print Solution().dpValue(n)
    print Solution().climbStairs(n)