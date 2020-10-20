#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/19 10:39 上午
@Author:  pulinghao
@File: 844. 比较含退格的字符串.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        stackS = []
        stackT = []
        for i in range(len(S)):
            if S[i] != '#':
                stackS.append(S[i])
            else:
                if len(stackS) > 0:
                    stackS.pop(-1)

        for i in range(len(T)):
            if T[i] != '#':
                stackT.append(T[i])
            else:
                if len(stackT) > 0:
                    stackT.pop(-1)

        if len(stackS) != len(stackT):
            return False
        else:
            for i in range(len(stackS)):
                if stackS[i] != stackT[i]:
                    return False

            return True


if __name__ == '__main__':
    S = "a#c"
    T = "b"
    out = Solution().backspaceCompare(S, T)

    print out
