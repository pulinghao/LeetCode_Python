#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/4 11:54 下午
 @Author   :pulinghao@baidu.com
 @File     :257. 二叉树的所有路径.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        path = []
        if root.left:
            for i in self.binaryTreePaths(root.left):
                path.append(str(root.val) + '->' + i)

        if root.right:
            for i in self.binaryTreePaths(root.right):
                path.append(str(root.val) + '->' + i)
        return path



if __name__ == '__main__':
    line = "[1,2,3,null,5]"
    root = leetcode_utils.stringToTreeNode(line)

    ret = Solution().binaryTreePaths(root)

    print ret