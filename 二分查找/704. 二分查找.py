#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/25 4:43 下午
 @Author   :pulinghao@baidu.com
 @File     :704. 二分查找.py 
 @Description :
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        return -1


if __name__ == '__main__':
    print  Solution().search(nums = [-1,0,3,5,9,12], target = 2)