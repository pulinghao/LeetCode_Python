#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/21 11:09 下午
 @Author   :pulinghao@baidu.com
 @File     :111. 二叉树的最小深度.py 
 @Description :
"""
import leetcode_utils
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return min(left, right) + 1

if __name__ == '__main__':
    line = "[1,2]"
    root = leetcode_utils.stringToTreeNode(line)
    print Solution().minDepth(root)