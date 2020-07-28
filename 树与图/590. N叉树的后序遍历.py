#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/25 9:52 下午
 @Author   :pulinghao@baidu.com
 @File     :590. N叉树的后序遍历.py 
 @Description :
"""

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def __init__(self):
        self.res = []
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 后序遍历，先左子节点，再跟节点
        if not root:
            return

        self.recursivePost(root)

    def recursivePost(self,node):
        if not node:
            return

        for child in node.children:
            self.recursivePost(child)
        self.res.append(node.val)
