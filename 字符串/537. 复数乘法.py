#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/30 12:21 下午
@Author:  pulinghao
@File: 537. 复数乘法.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = a.split('+')
        num_b = b.split('+')

        a = num_a[0]
        bstr = num_a[1]
        b = bstr[:-1]

        c = num_b[0]
        dstr = num_b[1]
        d = dstr[:-1]

        e = int(a) * int(c)  # 首项
        f = int(a) * int(d) + int(b) * int(c) # i前面的系数
        g = int(b) * int(d)  # i方前面的系数

        first = e - g
        res = str(first) + '+' + str(f) + 'i'
        return res

if __name__ == '__main__':
    out = Solution().complexNumberMultiply( "1+1i", "1+1i")
    print out 