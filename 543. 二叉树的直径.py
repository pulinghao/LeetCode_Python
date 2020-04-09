#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/8 11:09 下午
 @Author   :pulinghao@baidu.com
 @File     :543. 二叉树的直径.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def __init__(self):
        self.maxNum = 0  #这块需要把每次的最大值保存起来

    def depth(self,node):
        if not node:
            return 0

        left = self.depth(node.left)
        right = self.depth(node.right)
        self.maxNum = max(self.maxNum,left + right)   # 把最大值保存起来
        return max(left,right) + 1  # 给上一步返回的应该是左子树或者右子树中的最长路径+这个根节点



    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)
        return self.maxNum


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().diameterOfBinaryTree(root)
    print out