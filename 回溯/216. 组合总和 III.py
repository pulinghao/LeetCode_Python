#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/11 2:56 下午
@Author:  pulinghao
@File: 216. 组合总和 III.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def dfs(array, path, start, res, target):
            if target == 0:
                if len(path) == k:
                    res.append(path[:])
                return

            if target < 0:
                return

            if len(path) == k:
                return

            for i in range(start, len(array)):
                sub = target - array[i]
                if sub < 0:
                    continue

                path.append(array[i])
                dfs(array, path, i + 1, res, sub)
                path.pop(-1)

        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        path = []
        res = []
        dfs(array,path,0,res,n)
        return res

if __name__ == '__main__':
    k = 3
    n = 9
    print Solution().combinationSum3(k,n)
