#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/27 10:24 上午
@Author:  pulinghao
@File: 200. 岛屿数量.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid, x, y):

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return

            if grid[x][y] == '0':
                return

            grid[x][y] = '0'
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dir in dirs:
                dir_x = dir[0] + x
                dir_y = dir[1] + y
                dfs(grid, dir_x, dir_y)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(grid, i, j)

        return cnt

if __name__ == '__main__':
    grid =[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]

    out = Solution().numIslands(grid)

    print out
