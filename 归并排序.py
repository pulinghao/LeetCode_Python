#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/11 11:44 下午
 @Author   :pulinghao@baidu.com
 @File     :归并排序.py 
 @Description :
"""


class Solution(object):
    def mergeTwo(self, nums1, nums2):
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < len(nums1):
            res.append(nums2[i])
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        return res

    def sort(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, start, end):
        """
        :type nums: List[int]
        :rtype: int
        """
        if start >= end:
            return

        mid = start + (end - start) / 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid + 1, end)
        # 核心是合并
        self.merge(nums,start,mid,end)


    def merge(self, nums, start, mid, end):
        temp = []
        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= end:
            temp.append(nums[j])
            j += 1

        for i in range(len(temp)):
            nums[start + i] = temp[i]


if __name__ == '__main__':
    print Solution().sort(nums = [4,5,1,2,3,8,7])
