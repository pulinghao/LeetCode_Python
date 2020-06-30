#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/24 2:10 下午
@Author:  pulinghao
@File: 16. 最接近的三数之和.py
@Software: PyCharm
"""

import leetcode_utils
import sys

class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = sys.maxint
        delta = sys.maxint
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1


            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                if sum == target:
                    return target
                elif sum < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    if abs(sum - target) < delta:
                        delta = abs(sum - target)
                        ans = sum
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                    if abs(sum - target) < delta:
                        delta = abs(sum - target)
                        ans = sum

        return ans



if __name__ == '__main__':
    out = Solution().threeSumClosest(nums = [1,1,1,0], target = -100)

    print out 