#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/25 4:13 下午
 @Author   :pulinghao@baidu.com
 @File     :归并排序.py 
 @Description :
"""


class Solution(object):
    def __init__(self):
        self.sortednums = []
        self.nums = []

    def mergeSort(self, nums):
        self.nums = nums
        self.sort(0, len(nums) - 1)
        return self.nums
        pass

    def sort(self, left, right):
        if left < right:
            mid = (left + right) / 2
            self.sort(left, mid)
            self.sort(mid + 1, right)
            self.merge(left, mid, right)
        pass

    def merge(self, left, mid, right):
        self.sortednums = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if self.nums[i] < self.nums[j]:
                self.sortednums.append(self.nums[i])
                i += 1
            else:
                self.sortednums.append(self.nums[j])
                j += 1

        while i <= mid:
            self.sortednums.append(self.nums[i])
            i += 1

        while j <= right:
            self.sortednums.append(self.nums[j])
            j += 1

        t = 0
        while left <= right:
            self.nums[left] = self.sortednums[t]
            t += 1
            left += 1
        pass


if __name__ == '__main__':
    print Solution().mergeSort(nums=[5, 4, 3, 2, 1])
