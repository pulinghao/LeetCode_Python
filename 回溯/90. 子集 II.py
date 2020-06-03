#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/3 11:26 下午
 @Author   :pulinghao@baidu.com
 @File     :90. 子集 II.py 
 @Description :
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        track = []
        def backtrack(nums,track,start):
            res.append(list(track))

            for i in range(start,len(nums)):
                if nums[i] == nums[i - 1] and i != start: # 第一个元素可以重复
                    continue

                track.append(nums[i])
                backtrack(nums,track,i + 1)
                track.pop(-1)

        backtrack(nums,track,0)
        return res

if __name__ == '__main__':
    print Solution().subsetsWithDup(nums= [1,2,2])