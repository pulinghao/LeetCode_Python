#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time:  23:15
# @Author:pulinghao
# @File：统计一个数字在排序数组中的出现的次数.py
# @Software: PyCharm


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        def binarysearch(nums, target, left):
            low = 0
            high = len(nums)
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    if left:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1

            if left:
                if low >= len(nums) or nums[low] != target:
                    return -1
                else:
                    return low
            else:
                if high < 0 or nums[high] != target:
                    return -1
                else:
                    return high

            if not data:
                return 0
            return binarysearch(data,k,0) - binarysearch(data,k,1) + 1 if binarysearch(data, k, 0)>=0 else 0

                pass
