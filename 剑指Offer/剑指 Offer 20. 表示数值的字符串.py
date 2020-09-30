#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/2 3:24 下午
@Author:  pulinghao
@File: 剑指 Offer 20. 表示数值的字符串.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        n = len(s)
        symbolIndex = []
        eIndex = []
        pointIndex = []
        for i in range(n):
            if s[i] == "+" or s[i] == "-":
                symbolIndex.append(i)
                if len(symbolIndex) > 2:
                    return False
            elif s[i] == "E" or s[i] == "e":
                eIndex.append(i)
                if len(eIndex) > 1:
                    return False
            elif s[i] == ".":
                pointIndex.append(i)
                if len(pointIndex) > 1:
                    return False
            elif "0" <= s[i] <= "9":
                continue
            else:
                return False

        for i in symbolIndex:
            if (i != 0 and (i - 1) not in eIndex) or i == n - 1:
                return False

        for i in eIndex:
            if i == 0 or (i - 1) in symbolIndex or i == n - 1:
                return False
            for j in pointIndex:
                if i < j:
                    return False

        for i in pointIndex:
            if (i == 0 or (i - 1) in symbolIndex or (i - 1) in eIndex) and (
                    i == n - 1 or (i + 1) in symbolIndex or (i + 1) in eIndex):
                return False

        return True

if __name__ == '__main__':


    out = Solution().isNumber("12e+5.4")

    print out
