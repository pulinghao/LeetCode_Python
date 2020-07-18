#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/15 11:20 上午
@Author:  pulinghao
@File: 1514. 概率最大的路径.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """

        if n == 0:
            return 0

        nodesArray = [[] for _ in range(n)]
        for i in range(len(edges)):
            # [终点,概率],索引为起点
            edge = edges[i]
            sNode = edge[0]
            eNode = edge[1]
            prob = succProb[i]
            link = [eNode,prob]
            node = nodesArray[sNode]
            node.append(link)
            node2 = nodesArray[eNode]
            link2 = [sNode,prob]
            node2.append(link2)


        # BFS
        queue = [[start,1]] # 这里把prob也存起来
        nodeSet = set()  #防止重复查找

        res = []
        ans = 0
        while len(queue) > 0:
            top = queue.pop(0)
            index = top[0]
            curProb = top[1]
            # 在nodesArray中找到这个点
            node = nodesArray[index]
            for i in range(len(node)):
                link = node[i]
                sNode = index
                eNode = link[0]
                prob = link[1]

                if eNode == end:
                    # 计算当前的prob
                    res.append(curProb)
                    ans = max(ans,prob * ans)
                    pass

                if (sNode, eNode) in nodeSet or (eNode,sNode) in nodeSet:
                    # 不需要添加set中
                    pass
                else:
                    nodeSet.add((sNode,eNode))
                    queue.append([eNode, curProb * prob])

        if len(res) > 0:
            return max(res)
        return 0



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)
    n = 5
    edges = [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]]
    succProb = [0.37, 0.17, 0.93, 0.23, 0.39, 0.04]
    start = 3
    end = 4
    out = Solution().maxProbability(n, edges, succProb, start, end)

    print out 