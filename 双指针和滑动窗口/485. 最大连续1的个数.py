#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/15 8:34 下午
 @Author  :pulinghao@baidu.com
 @File     :485. 最大连续1的个数.py
 @Description :
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                res = max(cnt, res)
                cnt = 0

        res = max(cnt, res)
        return res

if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    print Solution().findMaxConsecutiveOnes(nums)