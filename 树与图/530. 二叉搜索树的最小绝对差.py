#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/12 10:58 上午
@Author:  pulinghao
@File: 530. 二叉搜索树的最小绝对差.py
@Software: PyCharm
"""

import leetcode_utils
import sys


class Solution(object):
    def __init__(self):
        self.res = sys.maxint
        pass

    def func(self, root):
        pass

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def midPost(root, res):
            if not root:
                return
            midPost(root.left, res)
            res.append(root.val)
            midPost(root.right, res)

        res = []
        midPost(root, res)
        for i in range(1, len(res)):
            if res[i] - res[i - 1] < self.res:
                self.res = res[i] - res[i - 1]
        return self.res


if __name__ == '__main__':
    line = "[1,null,3,2]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().getMinimumDifference(root)

    print out
