#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/16 10:47 下午
 @Author  :pulinghao@baidu.com
 @File     :561. 数组拆分 I.py
 @Description :
"""


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1.从小到大排列
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res

if __name__ == '__main__':
    nums = [6,2,6,5,1,2]
    print Solution().arrayPairSum(nums)
