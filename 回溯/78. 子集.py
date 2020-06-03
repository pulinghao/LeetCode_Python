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

        def backtrack(nums, start, track):
            self.res.append(list(track))
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i + 1, track)
                track.pop(-1)

        backtrack(nums, 0, track)
        return self.res


if __name__ == '__main__':
    print Solution().subsets(nums=[1, 2, 3])
