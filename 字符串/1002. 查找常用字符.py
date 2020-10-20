#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/14 10:49 上午
@Author:  pulinghao
@File: 1002. 查找常用字符.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        chars = [0] * 26
        for c in A[0]:
            chars[ord(c) - ord('a')] += 1

        for i in range(1, len(A)):
            temp = [0] * 26
            for c in A[i]:
                temp[ord(c) - ord('a')] += 1

            for j in range(len(chars)):
                chars[j] = min(chars[j], temp[j])

        res = []
        for i in range(len(chars)):
            if chars[i] > 0:
                for j in range(chars[i]):
                    res.append(chr(ord('a') + i))

        return res


if __name__ == '__main__':
    A = ["cool","lock","cook"]

    out = Solution().commonChars(A)

    print out
