#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/9/9 11:52 下午
 @Author  :pulinghao@baidu.com
 @File     :39. 组合总和.py
 @Description :
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break

                dfs(candidates, index, size, path + [candidates[index]], res, residue)

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    print Solution().combinationSum(candidates,target)