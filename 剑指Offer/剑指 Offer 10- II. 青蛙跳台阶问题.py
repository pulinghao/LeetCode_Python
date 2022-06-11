#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time:  09:25
# @Author:pulinghao
# @File：剑指 Offer 10- II. 青蛙跳台阶问题.py
# @Software: PyCharm


class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1:
            return 1
        temp1 = 1
        temp2 = 1
        for i in range(2,n + 1):
            temp3 = temp1 + temp2
            temp1 = temp2
            temp2 = temp3
        return temp2 % 1000000007


if __name__ == '__main__':
    a = 'A'|' '
    print a
    B = 'b'&'_'
    print B


