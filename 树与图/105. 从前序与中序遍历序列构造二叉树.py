#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/23 6:13 下午
 @Author   :pulinghao@baidu.com
 @File     :105. 从前序与中序遍历序列构造二叉树.py 
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # 前序遍历的构造 [root,left,right]
        # 中序遍历的构造 [left,root,right]
        # 所以只要用递归的方法,分别找到root，left，right，再递归调用即可

        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        # 找出前序遍历中的左序列，右序列
        left_index_in = inorder.index(preorder[0])
        left_preorder = preorder[1:left_index_in + 1]
        right_preorder= preorder[left_index_in + 1:]

        left_inorder = inorder[0:left_index_in]
        right_inorder = inorder[left_index_in + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

if __name__ == '__main__':
    line = "[3,9,20,15,7]"
    preorder = leetcode_utils.stringToIntegerList(line)
    line = "[9,3,15,20,7]"
    inorder = leetcode_utils.stringToIntegerList(line)

    ret = Solution().buildTree(preorder, inorder)

    out = leetcode_utils.treeNodeToString(ret)
    print out