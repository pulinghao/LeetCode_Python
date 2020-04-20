#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/20 6:55 下午
@Author:  pulinghao
@File: 236. 二叉树的最近公共祖先.py
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

        if not root:
            return None

        if root.val == q.val or root.val == p.val:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        # 左侧未找到，说明在右子树里
        if not left:
            return right

        # 右侧未找到，说明在左子树里
        if not right:
            return left

        if left and right:
            return root

        return None



if __name__ == '__main__':
    line = "[3,5,1,6,2,0,8,null,null,7,4]"
    root = leetcode_utils.stringToTreeNode(line)
    line = "[5]"
    # p = leetcode_utils.stringToInt(line)
    p_node = leetcode_utils.stringToTreeNode(line)
    line = "[1]"
    # q = leetcode_utils.stringToInt(line)
    q_node = leetcode_utils.stringToTreeNode(line)
    ret = Solution().lowestCommonAncestor(root, p_node, q_node)

    out = leetcode_utils.treeNodeToString(ret)
    print out
