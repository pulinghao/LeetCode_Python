#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/6 6:33 下午
@Author:  pulinghao
@File: 695. 岛屿的最大面积.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(self.dfs(grid,i,j),ans)
        return ans

    def dfs(self, grid, x, y):
        if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
            # 这里过滤掉grid[x][y] = 0的情况，避免增加计算量
            return 0

        grid[x][y] = 0
        ans = 1
        pairs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for dir in pairs:
            x_dir = dir[0]
            y_dir = dir[1]
            ans += self.dfs(grid, x + x_dir, y + y_dir)
        return ans



if __name__ == '__main__':
    grid =[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]
           ]

    out = Solution().maxAreaOfIsland(grid)

    print out
