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
        self.fa = {}
        self.vis = {}
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
        # 方法1.递归
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

    # 方法2:
    def lowestCommonAncestor2(self, root, p, q):
        self.fa[(root.val)] = None # 根节点的父节点为空
        self.dfs(root)
        while p:
            self.vis[p.val] = True;
            p = self.fa[p.val] #获取P的父节点

        while q:
            if q.val in self.vis.keys():
                return q
            q = self.fa[q.val]
        pass

    def dfs(self,node):
        if node.left:
            self.fa[(node.left.val)] = node
            self.dfs(node.left)
        if node.right:
            self.fa[(node.right.val)] = node
            self.dfs(node.right)



if __name__ == '__main__':
    line = "[3,5,1,6,2,0,8,null,null,7,4]"
    root = leetcode_utils.stringToTreeNode(line)
    line = "[5]"
    # p = leetcode_utils.stringToInt(line)
    p_node = leetcode_utils.stringToTreeNode(line)
    line = "[1]"
    # q = leetcode_utils.stringToInt(line)
    q_node = leetcode_utils.stringToTreeNode(line)
    ret = Solution().lowestCommonAncestor2(root, p_node, q_node)

    out = leetcode_utils.treeNodeToString(ret)
    print out
