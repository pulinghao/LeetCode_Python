#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/1/14 11:27 上午
@Author:  pulinghao
@File: 1018. 可被 5 整除的二进制前缀.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        num = 0
        for a in A:
            num = (num + a) * 2
            if num % 5 == 0:
                res.append(True)
            else:
                res.append(False)

        return res

if __name__ == '__main__':
    A = [0,1,1,1,1,1]
    out = Solution().prefixesDivBy5(A)
    print out
