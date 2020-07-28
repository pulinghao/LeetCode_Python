#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/25 9:44 下午
 @Author   :pulinghao@baidu.com
 @File     :173. 二叉搜索树迭代器.py 
 @Description :
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.idx = -1
        self.sortedArray = []
        self._order(root)

    def _order(self,node):
        if not node:
            return
        # 递归构造二叉搜索树
        self._order(node.left)
        self.sortedArray.append(node.val)
        self._order(node.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        self.idx += 1
        return self.sortedArray[self.idx]

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.idx + 1 < len(self.sortedArray):
            return True
        else:
            return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()