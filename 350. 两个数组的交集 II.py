#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/13 12:20 下午
@Author:  pulinghao
@File: 350. 两个数组的交集 II.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        for num in nums1:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        res = []
        for num in nums2:
            if num in dict:
                if dict[num] > 0:
                    res.append(num)
                    dict[num] -= 1

        return res


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().intersect(nums1 = [4,9,5], nums2 = [])

    print out 