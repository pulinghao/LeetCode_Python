#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/29 4:15 下午
@Author:  pulinghao
@File: 347. 前 K 个高频元素.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1.开辟K个空间
        array = []
        brray = []
        for i in range(nums[-1] + 1):
            array.append(0)
            brray.append([])

        for i in nums:
            array[i] += 1


        for i in range(len(array)):
            temp = brray[array[i]]
            temp.append(i)
            pass

        res = []
        for i in range(len(brray) - 1, -1, -1):
            temp = brray[i]
            if len(temp) > 0:
                for num in temp:
                    res.append(num)
            if len(res) == k:
                break

        return res




if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().topKFrequent(nums = [1,1,1,2,2,3],k = 1)

    print out 