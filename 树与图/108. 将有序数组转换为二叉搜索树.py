#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/3 10:53 上午
@Author:  pulinghao
@File: 108. 将有序数组转换为二叉搜索树.py
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

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedTree(nums)

    def sortedTree(self, nums):
        if len(nums) == 0:
            return None

        mid = len(nums) / 2
        node = TreeNode(nums[mid])
        left = nums[:mid]
        right = nums[mid + 1:]

        node.left = self.sortedTree(left)
        node.right = self.sortedTree(right)

        return node


if __name__ == '__main__':
    line = "[-10,-3,0,5,9]"
    nums = [-10, -3, 0, 5, 9]
    tree = Solution().sortedArrayToBST(nums)
    out = leetcode_utils.treeNodeToString(tree)
    print out
