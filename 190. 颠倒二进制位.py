#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/29 11:01 下午
 @Author  :pulinghao@baidu.com
 @File     :190. 颠倒二进制位.py
 @Description :
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            # 取n的最后一位
            last = n & 1
            # res 左移一位
            res = res << 1
            # 两者相加
            res = res | last
            n = n >> 1

        return res