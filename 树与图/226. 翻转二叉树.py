#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/12 5:46 下午
 @Author   :pulinghao@baidu.com
 @File     :226. 翻转二叉树.py 
 @Description :
"""
import leetcode_utils
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.invert(root)

    def invert(self, node):
        if not node:
            return node

        left = self.invert(node.left)
        right = self.invert(node.right)

        node.left = right
        node.right = left
        return node

if __name__ == '__main__':
    line = "[4,2,7,1,3,6,9]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().invertTree(root)
    out = leetcode_utils.treeNodeToString(ret)
    print out
