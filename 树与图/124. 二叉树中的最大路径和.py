#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/21 5:17 下午
 @Author   :pulinghao@baidu.com
 @File     :124. 二叉树中的最大路径和.py 
 @Description :
"""

import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = -sys.maxint
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def recursiveMaxPath(node):
            if not node:
                return 0

            left = 0
            right = 0
            if node.left:
                left = max(recursiveMaxPath(node.left), 0)
            if node.right:
                right = max(recursiveMaxPath(node.right), 0)

            # 把全局最优解保存下来
            self.res = max(self.res, node.val + left + right)

            # 返回的是局部最优解
            return node.val + max(left, right)

        recursiveMaxPath(root)
        return self.res