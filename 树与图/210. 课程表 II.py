#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/16 5:55 下午
@Author:  pulinghao
@File: 210. 课程表 II.py
@Software: PyCharm
"""

import leetcode_utils
import collections


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        queue = []
        res = []
        if len(prerequisites) == 0:
            for i in range(numCourses):
                res.append(i)
            return res

        dict = collections.defaultdict(list)
        dict2 = collections.defaultdict(list)
        for i in range(numCourses):
            dict[i] = []
            dict2[i] = []
        for i in range(len(prerequisites)):
            pre = prerequisites[i]
            class1 = pre[0]
            class2 = pre[1]
            dict[class1].append(class2)
            dict2[class2].append(class1)

        for i in range(numCourses):
            if len(dict[i]) == 0:
                queue.append(i)

        while len(queue):
            cur = queue.pop(0)
            res.append(cur)
            classes = dict2[cur]
            for cl in classes:
                dict[cl].remove(cur)
                if len(dict[cl]) == 0:
                    queue.append(cl)

        if len(res) != numCourses:
            return []
        return res

    def findOrder2(self, numCourses, prerequisites):
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses
        res = []
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        # 保存入度为0的点
        queue = collections.deque(u for u in range(numCourses) if indeg[u] == 0)

        while queue:
            top = queue.popleft()
            res.append(top)



if __name__ == '__main__':
    numCourses = 3
    prerequisites = [[0, 1], [0, 2], [1, 2]]
    print Solution().findOrder(numCourses, prerequisites)
