#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/5 10:55 下午
 @Author   :pulinghao@baidu.com
 @File     :1219. 黄金矿工.py 
 @Description :
"""


class Solution(object):
    def __init__(self):
        self.ans = 0
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        res = []
        track = []

        def isValid(i, j, grid):
            # 判断周围是否还能走
            if grid[i][j] == 0:
                return False
            else:
                return True

        def backtrack(grid, i, j, track):
            if not isValid(i, j, grid):
                res.append(list(track))
                self.ans = max(self.ans, sum(track))
                return

            for k in range(4):
                track.append(grid[i][j])
                grid[i][j] = 0
                if k == 0:
                    backtrack(grid, i, j - 1, track)
                elif k == 1:
                    backtrack(grid, i, j + 1, track)
                elif k == 2:
                    backtrack(grid, i - 1, j, track)
                else:
                    backtrack(grid, i + 1, j, track)
                num = track.pop(-1)
                grid[i][j] = num

        m = len(grid)
        n = len(grid[0])
        new_grid = []
        for i in range(m + 2):
            row = []
            for j in range(n + 2):
                if i == 0 or i == m + 1:
                    row.append(0)
                else:
                    if j == 0 or j == n + 1:
                        row.append(0)
                    else:
                        row.append(grid[i - 1][j - 1])
            new_grid.append(row)

        # 从左上角开始
        for i in range(1,m + 2):
            for j in range(1, n + 2):
                if new_grid[i][j] != 0:
                     backtrack(new_grid, i, j, track)
        return self.ans


if __name__ == '__main__':
    print Solution().getMaximumGold(grid=[[0,6,0],[5,8,7],[0,9,0]])
