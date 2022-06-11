#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/25 3:17 下午
 @Author   :pulinghao@baidu.com
 @File     :二分查找原形.py 
 @Description :
 参考labuladong帖子：
 https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/er-fen-cha-zhao-xiang-jie
"""

class Solution:
    # 最基本的模板
    def binarySearch(self, nums, key):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == key:
                return nums[mid]
            elif nums[mid] < key:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def  binarySearch2(self, nums, key):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == key:
                return nums[mid]
            elif nums[mid] < key:
                left = mid + 1
            else:
                right = mid - 1

        return left if nums[left] == key else -1

    #
    def wrong_binarySearch(self, nums, key):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == key:
                return nums[mid]
            elif nums[mid] < key:
                left = mid + 1  # 没有+1,mid的值其实被检索过了，应该加1；否则的话，指针始终停在left值
            else:
                right = mid # 没有-1,否则的话，right值始终等于left

        return -1

    # 查找左侧区间
    def left_bound(self, nums, key):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == key:
                right = mid
            elif nums[mid] > key:
                left = mid + 1
            elif nums[mid] < key:
                right = mid

        return left


    # 查找右侧
    def left_bound(self, nums, key):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == key:
                left = mid + 1
            elif nums[mid] > key:
                left = mid + 1
            elif nums[mid] < key:
                right = mid

        if left == 0:
            return -1

        return left - 1



if __name__ == '__main__':
    print Solution().wrong_binarySearch(nums=[1,2],key = 0)
    print Solution().binarySearch(nums=[1,2,3,5,7,8,10],key = 4)