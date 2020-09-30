#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/12 10:11 下午
 @Author   :pulinghao@baidu.com
 @File     :701. 二叉搜索树中的插入操作.py 
 @Description :
"""

import leetcode_utils


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

    def insertIntoBST2(self, root, val):
        def insert(root, val):
            if not root:
                root = TreeNode(val)
                return root
            if root.val < val:
                root.right = insert(root.right, val)
            else:
                root.left = insert(root.left, val)
            return root

        return insert(root, val)


if __name__ == '__main__':
    line = "[4,2,7,1,3]"
    val = 5
    root = leetcode_utils.stringToTreeNode(line)
    out = Solution().insertIntoBST2(root, val)
    outstr = leetcode_utils.treeNodeToString(out)
    print outstr
