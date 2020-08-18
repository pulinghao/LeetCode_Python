#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/12 10:26 下午
 @Author   :pulinghao@baidu.com
 @File     :700. 二叉搜索树中的搜索.py 
 @Description :
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)