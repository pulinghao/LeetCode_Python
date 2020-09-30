#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/10 5:28 下午
@Author:  pulinghao
@File: 40. 组合总和 II.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, path, start, res, target):
            if target == 0:
                res.append(path[:])
                return
            elif target < 0:
                return

            for i in range(start, len(candidates)):
                if i - 1 >= start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                sub = target - candidates[i]
                dfs(candidates, path, i + 1, res, sub)
                path.pop(-1)
        res = []
        path = []
        candidates.sort()
        dfs(candidates, path, 0, res, target)
        return res


if __name__ == '__main__':
    candidates =[2,5,2,1,2]
    target = 5
    print Solution().combinationSum2(candidates,target)
