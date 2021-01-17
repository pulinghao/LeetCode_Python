#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/11/29 10:08 下午
 @Author  :pulinghao@baidu.com
 @File     :976. 三角形的最大周长.py
 @Description :
"""

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            if  A[i - 2] + A[i - 1] > A[i]:
                return A[i - 2] + A[i - 1] + A[i]

        return 0

