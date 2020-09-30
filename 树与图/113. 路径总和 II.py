#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/27 1:07 下午
@Author:  pulinghao
@File: 113. 路径总和 II.py
@Software: PyCharm
"""

import leetcode_utils


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def dfs(node, sum, path, res):
            if sum == 0 and not node.left and not node.right:
                res.append(path[:])
                return

            if not node:
                return


            if node.left:
                path.append(node.left.val)
                dfs(node.left, sum - node.left.val, path, res)
                path.pop(-1)

            if node.right:
                path.append(node.right.val)
                dfs(node.right, sum - node.right.val, path, res)
                path.pop(-1)
            pass

        if not root:
            return []
        path = [root.val]
        res = []
        dfs(root, sum - root.val, path, res)
        return res


if __name__ == '__main__':
    line = "[-2,null,-3]"
    root = leetcode_utils.stringToTreeNode(line)
    sum = -5
    out = Solution().pathSum(root, sum)

    print out
