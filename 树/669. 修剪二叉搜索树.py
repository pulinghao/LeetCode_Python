#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/19 3:11 下午
 @Author   :pulinghao@baidu.com
 @File     :669. 修剪二叉搜索树.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # 1.BST 根节点 >= 左子树 ，根节点 <= 右子树
        if not root:
            return None

        if root.val > R:
            return self.trimBST(root.left,L,R)
        if root.val < L:
            return self.trimBST(root.right,L,R)

        root.left = self.trimBST(root.left,L,R)
        root.right = self.trimBST(root.right,L,R)
        return root



if __name__ == '__main__':
    line = "[1,0,2]"
    root = leetcode_utils.stringToTreeNode(line)
    line = "1"
    L = leetcode_utils.stringToInt(line)
    line = "2"
    R = leetcode_utils.stringToInt(line)

    ret = Solution().trimBST(root, L, R)

    out = leetcode_utils.treeNodeToString(ret)
    print out