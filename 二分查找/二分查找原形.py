#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/25 3:17 下午
 @Author   :pulinghao@baidu.com
 @File     :二分查找原形.py 
 @Description :
"""

class Solution:
    def binarySearch(self, nums, key):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == key:
                return nums[mid]
            elif nums[mid] < key:
                left = mid + 1
            else:
                right = mid

        return -1

        pass



if __name__ == '__main__':
    print Solution().binarySearch(nums=[1,2,3,5,7,8,10],key = 4)