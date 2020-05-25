#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/24 3:24 下午
 @Author   :pulinghao@baidu.com
 @File     :4. 寻找两个正序数组的中位数.py 
 @Description :
"""

import sys


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 1.将较长的数组放到nums2中
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        m = len(nums1)
        n = len(nums2)
        totalLeft = (m + n + 1) / 2  # 获取符合条件的k

        # 1.在nums1中找到分割线,满足交叉小于
        # 使得 nums1[i-1]<=nums2[j] && nums2[j - 1] <= nums1[i]
        # i：nums1右边数组第一个元素, j:nums2右边数组第一个元素
        # i j满足 i + j = (m + n + 1)/2
        left = 0
        right = m
        while left < right:
            i = left + (right - left + 1) / 2
            j = totalLeft - i
            if nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                left = i

        i = left
        j = totalLeft - i
        nums1LeftMax = nums1[i - 1] if i != 0 else -sys.maxint
        nums2LeftMax = nums2[j - 1] if j != 0 else -sys.maxint
        nums1RightMin = nums1[i] if i != m else sys.maxint
        nums2RightMin = nums2[j] if j != n else sys.maxint

        if (m + n) % 2 == 1:
            return max(nums1LeftMax, nums2LeftMax)
        else:
            return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin,nums2RightMin)) * 1.0 / 2


if __name__ == '__main__':
    print Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2])
