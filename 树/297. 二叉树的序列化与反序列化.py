#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/16 10:23 上午
@Author:  pulinghao
@File: 297. 二叉树的序列化与反序列化.py
@Software: PyCharm
"""

import leetcode_utils
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 层序遍历


        queue = deque()
        queue.append(root)
        res = []
        while len(queue):
            node = queue.popleft()
            if not node:
                res.append("null")
            else:
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)

        resStr = "["
        for i,item in enumerate(res):
            if item != "null":
                if i == len(res) - 1:
                    resStr += str(item) +']'
                else:
                    resStr += str(item) + ','
            else:
                if i == len(res) - 1:
                    resStr += 'null]'
                else:
                    resStr += 'null,'
        return resStr




    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 利用字符串构造一棵树
        str = data[1:-1]
        if len(str) == 0:
            return None
        array = str.strip().split(',')
        index = 0
        queue = deque()
        root = TreeNode(array[0])
        queue.appendleft(root)
        while index < len(array) and len(queue) != 0:
            node = queue.popleft()

            left_index = 2 * index + 1
            right_index = 2 * (index + 1)

            if left_index < len(array):
                if array[left_index] != "null":
                    left_value = array[left_index]
                    leftNode = TreeNode(left_value)
                    node.left = leftNode
                    queue.append(leftNode)
            else:
                break

            if right_index < len(array):
                if array[right_index] != "null":
                    right_value = array[right_index]
                    rightNode = TreeNode(right_value)
                    node.right = rightNode
                    queue.append(rightNode)
            else:
                break

            index += 1
        return root


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


if __name__ == '__main__':
    treeLine = "[1,2,3,null,null,4,5]"
    empty = "[]"
    node = Codec().deserialize(empty)
    res = Codec().serialize(node)
    print res
    # res = Codec().deserialize(treeLine)
    # print res
    tree = leetcode_utils.stringToTreeNode(treeLine)
    mytree = Codec().deserialize(treeLine)
    # print Codec().serialize(tree)
    print leetcode_utils.treeNodeToString(mytree)