#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/4/12 7:04 下午
@Author:  pulinghao
@File: 179. 最大数.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num_str = map(str, nums)

        compare = lambda x, y: 1 if x + y < y + x else -1
        num_str.sort(compare)
        res = "".join(num_str)
        if res[0] == "0":
            res = "0"
        return res


if __name__ == '__main__':
    nums = [3,30,34,5,9]
    out = Solution().largestNumber(nums)
    print out
