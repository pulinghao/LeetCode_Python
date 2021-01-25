#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/1/22 1:25 下午
@Author:  pulinghao
@File: 989. 数组形式的整数加法.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        B = []
        while K != 0:
            B.append(K % 10)
            K = K / 10
        C = []
        for num in range(len(B) - 1, -1, -1):
            C.append(B[num])

        res = []

        count = 0
        if len(C) > len(A):
            temp = A
            A = C
            C = temp

        for i in range(len(C)):
            add = A[-i - 1] + C[-i - 1] + count
            if add >= 10:
                add = add - 10
                count = 1
            else:
                count = 0
            res.append(add)

        for i in range(len(C), len(A)):
            add = A[-i - 1] + count
            if add >= 10:
                add = add - 10
                count = 1
            else:
                count = 0
            res.append(add)

        if count == 1:
            res.append(count)

        return res[::-1]


if __name__ == '__main__':
    A = [9,9,9]
    K = 1
    out = Solution().addToArrayForm(A, K)

    print out
