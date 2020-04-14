#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/14 2:48 下午
@Author:  pulinghao
@File: 437. 路径总和 III.py
@Software: PyCharm
"""


import leetcode_utils
class Solution(object):
    def __init__(self):
        self.count = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # 双递归思路
        # 1. 外层递归每个节点
        # 2. 对每个节点做递归
        # self.findEach(root, sum)
        self.bfs(root,sum)
        return self.count

        pass

    def findEach(self,node, sum):
        if not node:
            return

        self.findSum(node,sum)
        self.findEach(node.left, sum - node.val)
        self.findEach(node.right, sum - node.val)

    def bfs(self, node, sum):
        if not node:
            return

        queue = [node]
        while len(queue):
            node = queue.pop(0)
            self.findSum(node,sum)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        pass

    def findSum(self, node, sum):
        if not node:
            return

        if node.val == sum:
            self.count += 1

        self.findSum(node.left, sum - node.val)
        self.findSum(node.right, sum - node.val)

if __name__ == '__main__':
    line = "[10,5,-3,3,2,null,11,3,-2,null,1]"
    root = leetcode_utils.stringToTreeNode(line)
    line = "8"
    sum = leetcode_utils.stringToInt(line)

    ret = Solution().pathSum(root, sum)

    print ret