#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/11/24 10:22 下午
 @Author  :pulinghao@baidu.com
 @File     :222. 完全二叉树的节点个数.py
 @Description :
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        self.cnt = 0
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def count(node):
            if node:
                self.cnt += 1

                if node.left:
                    count(node.left)

                if node.right:
                    count(node.right)

        count(root)
        return self.cnt

if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)
    res = Solution().countNodes(root)
    print res
