#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/4/13 5:18 下午
@Author:  pulinghao
@File: 783. 二叉搜索树节点最小距离.py
@Software: PyCharm
"""

import leetcode_utils
import sys

class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 1.中序遍历
        stack = []
        res = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        ans = sys.maxint
        for i in range(1,len(res)):
            ans = min(ans,res[i] - res[i - 1])
        return ans


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().func(root)

    print out
