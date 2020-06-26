#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/25 6:13 下午
 @Author   :pulinghao@baidu.com
 @File     :852. 山脉数组的峰顶索引.py 
 @Description :
"""

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = l + (r -l) / 2

            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
                l = mid + 1
            elif A[mid] < A[mid - 1] and A[mid + 1] < A[mid]:
                r = mid - 1


if __name__ == '__main__':
    print Solution().peakIndexInMountainArray([0,1,0])