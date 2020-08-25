#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/8/24 6:30 下午
@Author:  pulinghao
@File: 459. 重复的子字符串.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        res = False
        for i in range(1, n / 2 + 1):
            if n % i == 0:
                temp = True
                for j in range(0, n / i - 1):
                    for k in range(i):
                        cur = k + j * i
                        next = k + (j + 1) * i
                        if s[cur] != s[next]:
                            temp = False
                            break
                    if temp == False:
                        break
            if temp == True:
                res = temp
                break

        return res


if __name__ == '__main__':
    s = "aba"
    print Solution().repeatedSubstringPattern(s)
