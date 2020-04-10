#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/8 10:30 下午
 @Author   :pulinghao@baidu.com
 @File     :110. 平衡二叉树.py 
 @Description :
"""
import leetcode_utils
class Solution(object):
    def balanced(self, node):
        if not node:
            return 0
        # 递归的思路
        # 1.左子树不是平衡树
        left = self.balanced(node.left)
        if left == -1:
            return -1

        # 2.右子树不是平衡树
        right = self.balanced(node.right)
        if right == -1:
            return -1

        # 3. 左子树的深度大于右子树
        if abs(left - right) > 1:
            return -1

        # 这块是难点，非常巧妙
        if left > right:
            return left + 1  # +1的意思是加上这个根节点（只有一个节点的树来说，深度是1)
        else:
            return right + 1



        pass

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return False if self.balanced(root) == -1 else True

if __name__ == '__main__':
    line = "[3,9,20,null,null,15,7]"
    root = leetcode_utils.stringToTreeNode(line)

    ret = Solution().isBalanced(root)

    out = (ret)
    print out