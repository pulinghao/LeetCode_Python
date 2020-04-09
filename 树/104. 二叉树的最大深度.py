#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/8 12:49 下午
@Author:  pulinghao
@File: 104. 二叉树的最大深度.py
@Software: PyCharm
"""

import leetcode_utils
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 1.递归思路
        # depth = 0
        # if root:
        #     depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # return depth
        # 一行流
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0

        # 2.深度遍历

if __name__ == '__main__':
    line = "[3,9,20,null,null,15,7]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().maxDepth(root)
    out = leetcode_utils.intToString(ret)
    print out
