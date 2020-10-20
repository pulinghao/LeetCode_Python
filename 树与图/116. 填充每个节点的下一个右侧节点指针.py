#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/15 10:16 上午
@Author:  pulinghao
@File: 116. 填充每个节点的下一个右侧节点指针.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        queue1 = [root]
        queue2 = []
        while len(queue1):
            cur = queue1.pop(0)
            if len(queue1) > 0:
                cur.next = queue1[0]
            else:
                cur.next = None

            if cur.left:
                queue2.append(cur.left)

            if cur.right:
                queue2.append(cur.right)

            if len(queue1) == 0:
                queue1 = queue2
                queue2 = []

        return root


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().connect(root)

    print out
