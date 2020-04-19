#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/17 8:11 下午
 @Author   :pulinghao@baidu.com
 @File     :687. 最长同值路径.py 
 @Description :
"""
import leetcode_utils


class Solution(object):
    def __init__(self):
        self.max = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.longPath(root)
        return self.max

    def longPath(self, node):
        if not node:
            return 0

        if not node.left and not node.right:
            return 0

        left_path = 0
        right_path = 0
        if node.left:
            left_length = self.longPath(node.left)
            if node.val == node.left.val:
                left_path = 1 + left_length

        if node.right:
            right_length = self.longPath(node.right)
            if node.val == node.right.val:
                right_path = 1 + right_length

        self.max = max(self.max, left_path + right_path)

        return max(left_path, right_path)


if __name__ == '__main__':
    line = "[5,4,5,1,1,5]"
    root = leetcode_utils.stringToTreeNode(line)

    ret = Solution().longestUnivaluePath(root)

    out = leetcode_utils.intToString(ret)
    print out
