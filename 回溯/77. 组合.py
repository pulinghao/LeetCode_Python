#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/4 8:06 下午
 @Author   :pulinghao@baidu.com
 @File     :77. 组合.py 
 @Description :
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        track = []
        nums = []
        for i in range(1, n + 1):
            nums.append(i)

        def backtrack(nums, track, start):
            if len(track) == k:
                res.append(list(track))

            for i in range(start,len(nums)):
                if nums[i] in track:
                    continue

                track.append(nums[i])
                backtrack(nums,track,i + 1)
                track.pop(-1)

        backtrack(nums,track,0)
        return res

if __name__ == '__main__':
    print Solution().combine(n = 4 , k = 2)