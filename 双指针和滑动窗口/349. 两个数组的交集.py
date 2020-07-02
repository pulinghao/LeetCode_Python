#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/30 8:05 下午
@Author:  pulinghao
@File: 349. 两个数组的交集.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        map = {}
        if len(nums2) > len(nums1):
            nums1,nums2 = nums2,nums1

        for num in nums1:
            map[num] = 1

        res = set()
        for num in nums2:
            if num in map:
                res.add(num)

        ans = list(res)
        return ans
if __name__ == '__main__':
    out = Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2])

    print out 