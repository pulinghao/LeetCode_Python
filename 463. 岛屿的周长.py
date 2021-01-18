#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/30 10:18 上午
@Author:  pulinghao
@File: 463. 岛屿的周长.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                island = grid[i][j]
                if island == 1:
                    add = 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        add -= 1
                    if i + 1 <= len(grid) - 1 and grid[i + 1][j] == 1:
                        add -= 1
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        add -= 1
                    if j + 1 <= len(grid[0]) - 1 and grid[i][j + 1] == 1:
                        add -= 1
                    res += add

        return res


if __name__ == '__main__':
    grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]


    out = Solution().islandPerimeter(grid)

    print out
