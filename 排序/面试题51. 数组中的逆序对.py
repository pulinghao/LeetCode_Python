#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/25 5:14 下午
 @Author   :pulinghao@baidu.com
 @File     :面试题51. 数组中的逆序对.py 
 @Description :
"""



class Solution(object):

    # 归并排序的思路
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.mergeSort(nums)
        print self.nums
        return self.cnt



    def __init__(self):
        self.sortednums = []
        self.cnt = 0
        self.nums = []

    def mergeSort(self, nums):
        self.nums = nums
        self.sort(0, len(nums) - 1)
        return self.cnt
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
            if self.nums[i] <= self.nums[j]:  #必须是等于，否则会多出来
                self.sortednums.append(self.nums[i])
                i += 1
            else:
                self.cnt += mid - i + 1 # 左侧，从第i个数到结尾，都比右侧第j个数大，构成逆序对
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
    print Solution().reversePairs(nums=[1,3,2,3,1])