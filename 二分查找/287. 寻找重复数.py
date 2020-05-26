#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/26 6:45 下午
@Author:  pulinghao
@File: 287. 寻找重复数.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 1
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) / 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt > mid:
                right = mid
            elif cnt == mid:
                left = mid + 1
            else:
                left = mid + 1
        return left
if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().func(root)

    print out 