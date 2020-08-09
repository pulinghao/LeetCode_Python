#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/7 12:12 上午
 @Author   :pulinghao@baidu.com
 @File     :100. 相同的树.py 
 @Description :
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            if not p and not q:
                return True
            else:
                return False