#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/28 10:13 下午
 @Author  :pulinghao@baidu.com
 @File     :724. 寻找数组的中心索引.py
 @Description :
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = [0]
        rightSum = [0]
        left = 0
        right = 0
        for i in range(len(nums)):
            left += nums[i]
            leftSum.append(left)
            right += nums[len(nums) - i - 1]
            rightSum.append(right)

        res = -1
        for i in range(len(nums)):
            l = leftSum[i]
            r = rightSum[len(nums) - i - 1]
            if l == r:
                res = i
                break

        return res


if __name__ == '__main__':
    nums = [-1,-1,0,0,-1,-1]
    print Solution().pivotIndex(nums)
