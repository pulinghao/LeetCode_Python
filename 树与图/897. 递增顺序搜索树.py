#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/4/25 5:00 下午
@Author:  pulinghao
@File: 897. 递增顺序搜索树.py
@Software: PyCharm
"""

import leetcode_utils
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        stack = [root]
        res = TreeNode()
        newCur = res
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop(-1)
            newCur.right = TreeNode(cur.val)
            newCur = newCur.right
            cur = cur.right

        return res.right

if __name__ == '__main__':
    line ="[5,3,6,2,4,null,8,1,null,null,null,7,9]"
    root = leetcode_utils.stringToTreeNode(line)

    outTree = Solution().increasingBST(root)
    out = leetcode_utils.treeNodeToString(outTree)
    print out
