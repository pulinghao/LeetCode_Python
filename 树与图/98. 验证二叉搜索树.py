#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/12 10:31 下午
 @Author   :pulinghao@baidu.com
 @File     :98. 验证二叉搜索树.py 
 @Description :
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __isValid(self, min, node, max):
        if not node:
            return True

        if min and node.val <= min.val:
            return False

        if max and node.val >= max.val:
            return False

        return self.__isValid(min,node.left,node) and self.__isValid(node,node.right,max)

        pass

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.__isValid(None,root,None)
