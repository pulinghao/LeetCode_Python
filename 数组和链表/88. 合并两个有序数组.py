#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/25 9:27 下午
 @Author   :pulinghao@baidu.com
 @File     :88. 合并两个有序数组.py 
 @Description :
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1

        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[k] = nums2[n - 1]
                n -= 1
            else:
                nums1[k] = nums1[m - 1]
                m -= 1
            k -= 1

        for i in range(n):
            nums1[i] = nums2[i]


if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution().merge(nums1,m,nums2,n)
    print nums1