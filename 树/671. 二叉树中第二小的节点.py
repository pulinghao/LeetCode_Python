#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/18 10:14 上午
 @Author   :pulinghao@baidu.com
 @File     :671. 二叉树中第二小的节点.py 
 @Description :
"""
import leetcode_utils
class Solution(object):
    def __init__(self):
        self.secondMin = 0
        self.blChangeSecMin = False
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        return self.recurseFind(root)

    def recurseFind(self, node, val):

        if node.val != val:
            return node.val

        if not node.left:
            return -1
        if node.left:
            left = self.recurseFind(node.left,val)

        if node.right:
            right = self.recurseFind(node.right,val)

        if left == -1:
            return right

        if right == -1:
            return left

        return min(left,right)



        pass
if __name__ == '__main__':
    line = "[2,2,5,null,null,5,7]"
    root = leetcode_utils.stringToTreeNode(line)

    ret = Solution().findSecondMinimumValue(root)

    out = leetcode_utils.intToString(ret)
    print out