#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/7 7:08 下午
@Author:  pulinghao
@File: 1343. 大小为 K 且平均值大于等于阈值的子数组数目.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        cnt = 0
        sum_array = sum(arr[:k])
        target = k * threshold
        if sum_array >= target:
            cnt += 1
        for i in range(k, len(arr)):
            sum_array += arr[i] - arr[i - k]
            if sum_array >= target:
                cnt += 1

        return cnt


if __name__ == '__main__':
    out = Solution().numOfSubarrays(arr=[7,7,7,7,7,7,7], k=7, threshold=7)

    print out
