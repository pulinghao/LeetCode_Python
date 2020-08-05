#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/8/4 12:34 下午
@Author:  pulinghao
@File: 207. 课程表.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        self.res = True
        pass

    def func(self, root):
        pass

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dict = {}

        for pair in prerequisites:
            left = pair[0]
            right = pair[1]
            if right in dict.keys():
                dict[right].append(left)
            else:
                dict[right] = [left]
        visited = [0] * numCourses
        for i in range(numCourses):
            if self.dfs(i,dict,visited):
                return False

        return True

    def dfs(self,node,dict,visited):
        """
        判断是否有环
        :param node:
        :param dict:
        :param visited:
        :return:
        """
        if visited[node] == 2:
            return True

        if visited[node] == 1:
            return False

        visited[node] = 2

        if node not in dict:
            visited[node] = 1
            return False

        for newnode in dict[node]:
            if self.dfs(newnode,dict,visited):
                return True
        visited[node] = 1
        return False

    def __dfs(self,node,path,dict):
        if node in path:
            return True  #有环

        path.append(node)
        subNodes = dict[node]
        for newNode in subNodes:
            if self.__dfs(newNode,path,dict):
                return True

        path.pop(-1)
        return False







if __name__ == '__main__':
    print Solution().canFinish(2,[[1,0]])