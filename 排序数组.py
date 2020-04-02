#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/31 1:38 下午
@Author:  pulinghao
@File: 排序数组.py
@Software: PyCharm https://leetcode-cn.com/problems/sort-an-array/
"""

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        return nums


if __name__ == '__main__':
    solve = Solution()
    print solve.sortArray(nums=[5,4,3,2,1,0,0])
