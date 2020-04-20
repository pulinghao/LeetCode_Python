#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/15 10:28 上午
@Author:  pulinghao
@File: 107. 二叉树的层次遍历 II.py
@Software: PyCharm
"""

import leetcode_utils
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue1 = [root]
        queue2 = []
        stack = []
        res = []

        line = []
        while len(queue1):
            node = queue1.pop(0)
            line.append(node.val)
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
            if len(queue1) == 0:
                queue1 = queue2
                queue2 = []
                stack.append(line)
                line = []

        while len(stack):
            res.append(stack.pop())
        return res

        pass


if __name__ == '__main__':
    line = "[3,9,20,null,null,15,7]"
    root = leetcode_utils.stringToTreeNode(line)

    ret = Solution().levelOrderBottom(root)

    out = leetcode_utils.int2dArrayToString(ret)
    print out