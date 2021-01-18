#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/1/13 8:36 下午
@Author:  pulinghao
@File: 684. 冗余连接.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self,n):

        pass

    def func(self, root):
        pass


    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def find(x):
            if fa[x] == x:
                return x
            else:
                return find(fa[x])

        def union(x,y):
            """
            把y接到x的父元素上
            :param x:
            :param y:
            :return:
            """
            fa[find(x)] = find(y)
        n = len(edges)
        fa = list(range(n + 1))
        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1,node2)
            else:
                return [node1,node2]

        return []


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().func(root)

    print out
