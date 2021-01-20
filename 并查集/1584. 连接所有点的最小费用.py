#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/19 11:29 下午
 @Author  :pulinghao@baidu.com
 @File     :1584. 连接所有点的最小费用.py
 @Description :
"""
import sys


class Union:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self,x):
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]


    def union(self,x,y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = Union(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))

        edges.sort()

        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.union(x, y):
                ret += length
                num += 1
                if num == n:
                    break

        return ret


if __name__ == '__main__':
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print Solution().minCostConnectPoints(points)
