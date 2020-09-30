#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/22 6:48 下午
@Author:  pulinghao
@File: 968. 监控二叉树.py
@Software: PyCharm
"""

import leetcode_utils

NO_CAMERA = 0
HAS_CAMERA = 1
NO_NEED = 2


class Solution(object):
    def __init__(self):
        self.res = 0
        pass

    def func(self, root):
        pass

    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return NO_NEED

            left = dfs(node.left)
            right = dfs(node.right)

            if left == NO_CAMERA or right == NO_CAMERA:
                self.res += 1
                return HAS_CAMERA

            return NO_NEED if left == HAS_CAMERA or right == HAS_CAMERA else NO_CAMERA

        if not root:
            return 0

        if dfs(root) == NO_CAMERA:
            self.res += 1
        return self.res


if __name__ == '__main__':
    line = "[0,0,null,0,0]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().minCameraCover(root)

    print out
