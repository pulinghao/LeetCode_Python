#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/23 10:55 上午
@Author:  pulinghao
@File: 67. 二进制求和.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1

        cnt = 0  # 表示进位
        res = []
        while i >= 0 and j >= 0:
            sum = int(a[i]) + int(b[j]) + cnt
            if sum >= 2:
                res.append(sum - 2)
                cnt = 1
            else:
                res.append(sum)
                cnt = 0
            i -= 1
            j -= 1

        while i >= 0:
            sum = int(a[i]) + cnt
            if sum >= 2:
                res.append(sum - 2)
                cnt = 1
            else:
                res.append(sum)
                cnt = 0
            i -= 1

        while j >= 0:
            sum = int(b[j]) + cnt
            if sum >= 2:
                res.append(sum - 2)
                cnt = 1
            else:
                res.append(sum)
                cnt = 0
            j -= 1

        if cnt == 1:
            res.append(cnt)
        res.reverse()

        resStr = ""
        for i in range(len(res)):
            resStr += str(res[i])
        return resStr


if __name__ == '__main__':
    print Solution().addBinary(a = "1010", b = "1011")

