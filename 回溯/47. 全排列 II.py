#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/31 10:49 下午
 @Author   :pulinghao@baidu.com
 @File     :47. 全排列 II.py 
 @Description :
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 1.先排序
        nums.sort()

        # 定义两个数组，一个记录结果，一个保存路径
        res = []
        track = []

        used = [False for i in range(len(nums))]
        def backtrack(nums,track,used):
            if len(nums) == len(track):
                res.append(list(track))
                return

            for i in range(len(nums)):
                # 设置去重条件
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    track.append(nums[i])
                    backtrack(nums,track,used)
                    track.pop()
                    used[i] = False

        backtrack(nums,track,used)
        return res

if __name__ == '__main__':
    print Solution().permuteUnique(nums=[1,1,2])