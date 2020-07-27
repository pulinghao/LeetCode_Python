#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/18 4:40 下午
@Author:  pulinghao
@File: 785. 判断二分图.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        self.valid = True
        pass

    def func(self, root):
        pass

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # 节点数量
        N = len(graph)
        # 染色 0:未染色 1:红色 2:蓝色
        colors = [0] * N


        def dfs(node, color, graph):
            colors[node] = color
            nextColor = 0
            if color == 1:
                # 如果是红色,下个点颜色涂蓝色
                nextColor = 2
            else:
                nextColor = 1

            for neighbour in graph[node]:
                if colors[neighbour] == 0:
                    dfs(neighbour, nextColor, graph)
                    if self.valid == False:
                        break
                elif colors[neighbour] != nextColor:
                    self.valid = False
                    break

            pass

        for i in range(N):
            if colors[i] == 0:
                dfs(i, 1, graph)

        return self.valid


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]])

    print out
