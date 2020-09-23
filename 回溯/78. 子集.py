#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/3 10:52 下午
 @Author   :pulinghao@baidu.com
 @File     :78. 子集.py 
 @Description :
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        track = []
        res = []

        def backtrack(nums, start, track, res):
            res.append(list(track))
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i + 1, track, res)
                track.pop(-1)

        backtrack(nums, 0, track, res)
        return res


if __name__ == '__main__':
    print Solution().subsets(nums=[1, 2, 3])
