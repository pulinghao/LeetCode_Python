#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/29 10:42 上午
@Author:  pulinghao
@File: 129. 求根到叶子节点数字之和.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, path, res):
            if not node.left and not node.right:
                temp = path[:]
                num_str = ''.join(str(i) for i in temp)
                res.append(int(num_str))
                return

            leafs = []
            if node.left:
                leafs.append(node.left)

            if node.right:
                leafs.append(node.right)

            for leaf in leafs:
                path.append(leaf.val)
                dfs(leaf, path, res)
                path.pop(-1)

        if not root:
            return 0
        res = []
        path = [root.val]
        dfs(root, path, res)
        return sum(res)


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().sumNumbers(root)

    print out
