#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/20 6:31 下午
@Author:  pulinghao
@File: 235. 二叉搜索树的最近公共祖先.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)

        if q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)

        return root


if __name__ == '__main__':
    line = "[6,2,8,0,4,7,9,null,null,3,5]"
    root = leetcode_utils.stringToTreeNode(line)
    line = "2"
    p = leetcode_utils.stringToInt(line)
    line = "8"
    q = leetcode_utils.stringToInt(line)

    ret = Solution().lowestCommonAncestor(root, p, q)

    out = leetcode_utils.treeNodeToString(ret)
    print out