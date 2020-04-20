#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/19 10:26 下午
 @Author   :pulinghao@baidu.com
 @File     :538. 把二叉搜索树转换为累加树.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def __init__(self):
        self.sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            self.sum += root.val
            root.val = self.sum
            self.convertBST(root.left)
        return root



if __name__ == '__main__':
    line = "[5,2,13]"
    root = leetcode_utils.stringToTreeNode(line)

    ret = Solution().convertBST(root)

    out = leetcode_utils.treeNodeToString(ret)
    print out