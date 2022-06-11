#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time:  16:09
# @Author:pulinghao
# @File：剑指 Offer 07. 重建二叉树.py
# @Software: PyCharm

import leetcode_utils

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 找到根节点
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = leetcode_utils.TreeNode(0)
        root.val = preorder[0]
        idx = inorder.index(root.val)
        leftInOrderList = inorder[:idx]
        rightInOrderList = inorder[idx + 1:]

        leftPreOrder = preorder[1:len(leftInOrderList) + 1]
        rightPreOrder = preorder[len(leftInOrderList) + 1 :]

        root.left = self.buildTree(leftPreOrder,leftInOrderList)
        root.right = self.buildTree(rightPreOrder,rightInOrderList)
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    outputNode = Solution().buildTree(preorder,inorder)
    output = leetcode_utils.treeNodeToString(outputNode)
    print output