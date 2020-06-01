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
        # 定义两个数组，一个记录结果，一个保存路径
        res = []

        new_nums = []
        for num in nums:
            if num in new_nums:
                continue
            else:
                new_nums.append(num)

        track = []    # 保留数值
        def backtrack(nums,new_nums,track):
            if len(nums) == len(track):
                res.append(list(track))
                return

            for i in range(len(new_nums)):
                if new_nums[i] in track:
                    continue

                track.append(new_nums[i])
                backtrack(nums,new_nums,track)
                track.pop(-1)


        backtrack(nums,new_nums,track)
        return res

if __name__ == '__main__':
    print Solution().permuteUnique(nums=[1,1,2])