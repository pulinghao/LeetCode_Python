#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/12 3:03 下午
 @Author   :pulinghao@baidu.com
 @File     :133. 克隆图.py 
 @Description :
"""
import leetcode_utils

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        newNode = Node()
        newNode.val = node.val
        newNeighbors = []

        self.visited[node] = newNode
        if node.neighbors:
            for neighbor in node.neighbors:
                newNeighbor = self.cloneGraph(neighbor)
                newNeighbors.append(newNeighbor)

        newNode.neighbors = newNeighbors
        return newNode



def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    # lines = readlines()
    while True:
        try:
            line = "[[2,4],[1,3],[2,4],[1,3]]"
            node = leetcode_utils.stringToInt2dArray(line)

            ret = Solution().cloneGraph(node)

            out = leetcode_utils.treeNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()