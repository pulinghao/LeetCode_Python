#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/8/25 4:29 下午
@Author:  pulinghao
@File: 491. 递增子序列.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        for i in range(len(nums)):
            path = []
            self.__dfs(nums, path, i, res)

        return res

    def recursive(self, nums):
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums[0]]

    def __dfs(self, nums, path, cur, res):
        # 1. 判断是否满足条件
        # 1）如果遍历数组到最后一个元素，就结束
        if cur == len(nums):
            # res.append(path[:])
            return

        path.append(nums[cur])
        if len(path) > 1:
            res.add(path)
        for i in range(cur + 1, len(nums)):
            if nums[i] > nums[cur]:
                self.__dfs(nums, path, i, res)
                path.pop(-1)
            pass


if __name__ == '__main__':
    print Solution().findSubsequences(nums=[4, 6, 7, 7])
