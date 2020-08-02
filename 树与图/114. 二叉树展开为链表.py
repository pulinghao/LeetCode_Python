#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/2 9:03 下午
 @Author   :pulinghao@baidu.com
 @File     :114. 二叉树展开为链表.py 
 @Description :
"""
import leetcode_utils
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.recursive(root)

        pass

    def recursive(self,node):
        if not node:
            return None

        left = node.left
        right = node.right

        node.left = None
        node.right = self.recursive(left)
        tail = self.recursive(right)
        cur = node
        while cur.right:
            cur = cur.right

        cur.right = tail
        return node

if __name__ == '__main__':
    line = "[1,2,5,3,4,null,6]"
    root = leetcode_utils.stringToTreeNode(line)

    Solution().flatten(root)
    print 'finish'