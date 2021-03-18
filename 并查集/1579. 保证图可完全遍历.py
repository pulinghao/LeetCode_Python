#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/27 10:22 下午
 @Author  :pulinghao@baidu.com
 @File     :1579. 保证图可完全遍历.py
 @Description :
"""


class UnionFind:
    def __init__(self, size):
        self.father = [None] * (size + 1)
        self.num_of_sets = size

    def find(self, x):
        if self.father[x] is None: return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        self.father[self.find(x)] = self.find(y)
        self.num_of_sets -= 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        for _type, n1, n2 in edges:
            if _type == 3:
                if not uf_alice.is_connected(n1, n2):
                    uf_alice.merge(n1, n2)
                    uf_bob.merge(n1, n2)
                else:
                    res += 1
        for _type, n1, n2 in edges:
            if _type == 1:
                if not uf_alice.is_connected(n1, n2):
                    uf_alice.merge(n1, n2)
                else:
                    res += 1
            if _type == 2:
                if not uf_bob.is_connected(n1, n2):
                    uf_bob.merge(n1, n2)
                else:
                    res += 1

        return -1 if uf_alice.num_of_sets * uf_bob.num_of_sets > 1 else res
