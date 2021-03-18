#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/31 8:53 下午
 @Author  :pulinghao@baidu.com
 @File     :1046. 最后一块石头的重量.py
 @Description :
"""
import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 初始化
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        # 模拟
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, x - y)

        if heap:
            return -heap[0]
        return 0