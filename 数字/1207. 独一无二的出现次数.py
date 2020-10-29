#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/28 11:15 上午
@Author:  pulinghao
@File: 1207. 独一无二的出现次数.py
@Software: PyCharm
"""

import leetcode_utils
import collections

class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = collections.defaultdict(int)
        for num in arr:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1
        dict2 = collections.defaultdict(int)
        res = True
        for key,value in dict.items():
            if value in dict2:
                res = False
                break
            else:
                dict2[value] = key
        return res


if __name__ == '__main__':
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    out = Solution().uniqueOccurrences(arr)

    print out
