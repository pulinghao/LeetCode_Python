#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/24 10:34 上午
@Author:  pulinghao
@File: 501. 二叉搜索树中的众数.py
@Software: PyCharm
"""

import leetcode_utils
import collections

class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def dfs(node, dic, res):
            if not node:
                return

            dic[node.val] += 1
            dfs(node.left, dic, res)
            dfs(node.right, dic, res)

        dic = collections.defaultdict(int)
        res = []
        dfs(root, dic, res)
        for k, v in dic.items():
            res.append([v, k])

        res.sort(key=lambda x: x[0], reverse=True)

        ans = []
        for i, v in enumerate(res):
            if i == 0:
                ans.append(v[1])
                continue

            if v[0] == res[0][0]:
                ans.append(v[1])

        return ans


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().func(root)

    print out
