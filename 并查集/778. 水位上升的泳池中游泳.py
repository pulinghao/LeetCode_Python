#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/30 10:33 下午
 @Author  :pulinghao@baidu.com
 @File     :778. 水位上升的泳池中游泳.py
 @Description :
"""


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[x_root] = y_root

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        n = len(grid)

        # 因为需要从小到大考虑时刻 t，从平台高度 t 出发判断是否能与相邻的方块连通
        # 所以这里需要存储每个平台高度对应的位置
        idx = [0] * (n * n)
        for i in range(n):
            for j in range(n):
                idx[grid[i][j]] = (i, j)

        print(idx)
        uf = UnionFind(n * n)
        for t in range(n * n):
            # 对高度为 t 的平台进行判断是否能与相邻四个方位的平台连通
            x, y = idx[t]
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] <= t:
                    # 尝试合并相邻的平台
                    uf.union(x * n + y, nx * n + ny)

            # 检查左下角与右下角是否连通，
            # 若能连通，此时的 t 即是答案
            if uf.connected(0, n * n - 1):
                return t

        return -1
