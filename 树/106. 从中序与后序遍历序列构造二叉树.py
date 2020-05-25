#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/24 10:28 下午
 @Author   :pulinghao@baidu.com
 @File     :106. 从中序与后序遍历序列构造二叉树.py 
 @Description :
"""

import leetcode_utils
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(postorder) == 0 or len(inorder) == 0:
            return None
        # 1.拿到root节点
        root = TreeNode(postorder[-1])

        left = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:left],postorder[:left])
        root.right = self.buildTree(inorder[left + 1:],postorder[left:-1])

        return root

if __name__ == '__main__':
    line = "[9,3,15,20,7]"
    inorder = leetcode_utils.stringToIntegerList(line)
    line = "[9,15,7,20,3]"
    postorder = leetcode_utils.stringToIntegerList(line)

    ret = Solution().buildTree(inorder, postorder)

    out = leetcode_utils.treeNodeToString(ret)
    print out