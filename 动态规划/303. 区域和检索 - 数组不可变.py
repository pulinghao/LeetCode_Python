#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/21 8:01 下午
@Author:  pulinghao
@File: 303. 区域和检索 - 数组不可变.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self,nums):
        i = 0
        self.list = [0]
        # 把各个区间的和加上
        while i < len(nums):
            last = self.list[-1]
            self.list.append(last + nums[i])
            i += 1
        pass

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.list[j + 1] - self.list[i]

if __name__ == '__main__':
    sol = Solution(nums = [-2, 0, 3, -5, 2, -1])
    out = sol.sumRange(2,5)

    print out 