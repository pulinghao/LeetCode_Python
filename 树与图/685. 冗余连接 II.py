#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/9/17 11:25 下午
 @Author  :pulinghao@baidu.com
 @File     :685. 冗余连接 II.py
 @Description :
"""


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)

        def check(cur):
            f = {}

            def find(x):
                f.setdefault(x, x)
                if f[x] != x:
                    x = find(f[x])
                return f[x]

            def union(x, y):
                f[find(y)] = find(x)

            for i in range(n):
                if i == cur:
                    continue
                if find(edges[i][0]) == find(edges[i][1]):
                    return True
                union(edges[i][0], edges[i][1])
            return False

        indegree = [0] * (n + 1)
        for x, y in edges:
            indegree[y] += 1

        for i in range(n - 1, - 1, -1):
            if indegree[edges[i][1]] == 2:
                if not check(i):
                    return edges[i]

        for i in range(n - 1, -1, -1):
            if indegree[edges[i][1]] == 1:
                if not check(i):
                    return edges[i]


if __name__ == '__main__':
    edges = [[1,2], [1,3], [2,3]]
    print Solution().findRedundantDirectedConnection(edges)