#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/12 10:11 下午
 @Author   :pulinghao@baidu.com
 @File     :701. 二叉搜索树中的插入操作.py 
 @Description :
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root