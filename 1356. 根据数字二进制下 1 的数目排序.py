#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/11/6 2:07 下午
@Author:  pulinghao
@File: 1356. 根据数字二进制下 1 的数目排序.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort()
        dict = []
        for num in arr:
            cnt = 0
            temp = num
            while num / 2:
                if num % 2 == 1:
                    cnt += 1
                num = num / 2
            if cnt in dict.keys():
                dict[cnt].append(temp)
            else:
                dict[cnt] = [temp]

        res = []
        

if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().func(root)

    print out
