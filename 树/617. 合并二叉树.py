#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/13 11:20 上午
@Author:  pulinghao
@File: 617. 合并二叉树.py
@Software: PyCharm
"""

import leetcode_utils

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 or not t2:
            return t2 if not t1 else t1

        queue = [(t1,t2)]
        while queue:
            r1,r2 = queue.pop(0)
            r1.val += r2.val

            if r1.left and r2.left:
                queue.append((r1.left,r2.left))
            elif not r1.left:
                # 令r1的节点为r2
                r1.left = r2.left

            if r1.right and r2.right:
                queue.append((r1.right,r2.right))
            elif not r1.right:
                r1.right = r2.right

        return t1




if __name__ == '__main__':
    line1 = "[1,3,2,5]"
    t1 = leetcode_utils.stringToTreeNode(line1)
    line2 = "[2,1,3,null,4,null,7]"
    t2 = leetcode_utils.stringToTreeNode(line2)

    ret = Solution().mergeTrees(t1, t2)

    out = leetcode_utils.treeNodeToString(ret)
    print out