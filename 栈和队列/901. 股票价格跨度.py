#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/27 3:54 下午
 @Author   :pulinghao@baidu.com
 @File     :901. 股票价格跨度.py 
 @Description :
"""

import copy
class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        idx = 1
        while self.stack and self.stack[-1][1] <= price:
            idx += self.stack[-1][0]
        self.stack.append((idx,price))
        return idx






