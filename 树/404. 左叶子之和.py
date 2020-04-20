#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/16 9:37 上午
@Author:  pulinghao
@File: 404. 左叶子之和.py
@Software: PyCharm
"""

import leetcode_utils

class Solution(object):
    def __init__(self):
        self.leftSum = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        if not root:
            return 0

        return self.sumLeft(root)


    def sumLeft(self,node):
        if not node:
            return 0

        if not node.left:
            return self.sumLeft(node.right)

        else:
            if not node.left.left and not node.left.right:  # 判断左子节点是否是叶子节点
                return node.left.val + self.sumLeft(node.right)
            else:
                return self.sumLeft(node.left) + self.sumLeft(node.right)


if __name__ == '__main__':
    line = "[3,9,20,null,null,15,7]"
    root = leetcode_utils.stringToTreeNode(line)

    ret = Solution().sumOfLeftLeaves(root)

    out = leetcode_utils.intToString(ret)
    print out