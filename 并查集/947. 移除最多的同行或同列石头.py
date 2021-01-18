#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/1/15 6:33 下午
@Author:  pulinghao
@File: 947. 移除最多的同行或同列石头.py
@Software: PyCharm
"""

import collections
import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        dictX = collections.defaultdict(list)
        dictY = collections.defaultdict(list)
        visited = set()
        for x,y in stones:
            dictX[x].append((x,y))
            dictY[y].append((x,y))

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for i in dictX[node[0]]:
                dfs(i)

            for i in dictY[node[1]]:
                dfs(i)

        ans = 0

        for stone in stones:
            # 这里需要转成元组
            tup = tuple(stone)
            if tup not in visited:
                ans += 1
                dfs(tup)
        return len(stones) - ans






if __name__ == '__main__':
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

    out = Solution().removeStones(stones)

    print out
