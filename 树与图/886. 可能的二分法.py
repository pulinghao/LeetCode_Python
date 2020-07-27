#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/18 5:05 下午
@Author:  pulinghao
@File: 886. 可能的二分法.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        self.valid = True
        pass

    def func(self, root):
        pass

    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if len(dislikes) == 0:
            return True

        # 1.建表
        table = {}
        valid = True
        for i in range(len(dislikes)):
            pair = dislikes[i]
            if pair[0] in table:
                people = table[pair[0]]
                people.append(pair[1])
            else:
                table[pair[0]] = [pair[1]]

            if pair[1] in table:
                people = table[pair[1]]
                people.append(pair[0])
            else:
                table[pair[1]] = [pair[0]]

        def dfs(node, color, graph):
            if node not in table:
                return
            colors[node] = color
            nextColor = 0


            pairs = table[node]
            if color == 1:
                nextColor = 2
            else:
                nextColor = 1

            for nextNode in pairs:
                if colors[nextNode] == 0:
                    dfs(nextNode,nextColor,dislikes)
                    if not self.valid:
                        break
                elif colors[nextNode] != nextColor:
                    self.valid = False
                    break

            pass

        colors = [0] * (N + 1)
        for i in range(1,N + 1):
            if colors[i] == 0:
                dfs(i, 1, dislikes)

        return self.valid


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().possibleBipartition(N = 10, dislikes = [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]])

    print out
