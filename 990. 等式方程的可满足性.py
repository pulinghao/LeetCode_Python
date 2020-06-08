#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/8 4:17 下午
@Author:  pulinghao
@File: 990. 等式方程的可满足性.py
@Software: 并查集思路
"""

import leetcode_utils
from collections import defaultdict

class Solution(object):
    def __init__(self):
        # 创建26个parent
        self.parent = list(range(26))
        pass

    def func(self, root):
        pass

    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        for i in range(len(equations)):
            eq = equations[i]
            if eq[1] == '=':
                # 如果相等，加入并查集
                a = ord(eq[0]) - ord('a')
                b = ord(eq[-1]) - ord('a')
                self.union(a,b)

        for i in range(len(equations)):
            eq = equations[i]
            if eq[1] == '!':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[-1]) - ord('a')
                if self.find(a) == self.find(b):
                    return False

        return True


    def find(self,node):
        if self.parent[node] == node:
            return node
        else:
            return self.find(self.parent[node]) #找到根节点
        pass

    def union(self,node1,node2):
        self.parent[self.find(node1)] = self.find(node2)




if __name__ == '__main__':
    out = Solution().equationsPossible(equations=["c==c","b==d","x!=z"])

    print out 