#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/16 2:39 下午
@Author:  pulinghao
@File: 589. N叉树的前序遍历.py
@Software: PyCharm
"""

import leetcode_utils


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def __init__(self):
        self.res = []
        pass

    def func(self, root):
        pass

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """


        # 递归
        # self.recursivePreorder(root)
        # return self.res
        # 迭代
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output



    def recursivePreorder(self,node):
        if not node:
            return

        self.res.append(node.val)

        for node in node.children:
            self.recursivePreorder(node)




if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().func(root)
    list = [1,2,3]
    antoher = list[::-1]
    print antoher