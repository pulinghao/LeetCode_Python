#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/11 10:50 下午
 @Author  :pulinghao@baidu.com
 @File     :703. 数据流中的第 K 大元素.py
 @Description :
"""

import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.queue = nums
        heapq.heapify(self.queue)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.queue,val)
        while len(self.queue) > self.k:
            heapq.heappop(self.queue)
        return self.queue[0]
