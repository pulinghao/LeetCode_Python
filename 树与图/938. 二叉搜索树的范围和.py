#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/26 3:44 下午
 @Author   :pulinghao@baidu.com
 @File     :938. 二叉搜索树的范围和.py 
 @Description :
"""
import leetcode_utils


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        def recursive(node, L, R):
            if not node:
                return

            if L <= node.val <= R:
                self.sum += node.val
                recursive(node.left, L, R)
                recursive(node.right, L, R)
            elif node.val < L:
                recursive(node.right, L, R)
            elif node.val > R:
                recursive(node.left, L, R)
            return

        recursive(root, L, R)
        return self.sum


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)
    L = 7
    R = 15
    ret = Solution().rangeSumBST(root, L, R)

    out = leetcode_utils.intToString(ret)
    print out
