#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/13 9:13 下午
 @Author   :pulinghao@baidu.com
 @File     :112. 路径总和.py 
 @Description :
"""
import leetcode_utils

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.recursive(root,sum)

    def recursive(self, node, sum):
        if not node:
            return False

        if not node.left and not node.right:
            if node.val == sum:
                return True
            else:
                return False
        else:
            rest = sum - node.val
            return self.recursive(node.left,rest) or self.recursive(node.right,rest)



if __name__ == '__main__':
    # line1 = "[5,4,8,11,null,13,4,7,2,null,null,null,1]"
    line1 = "[]"
    root = leetcode_utils.stringToTreeNode(line1)
    line2 = 22
    sum = leetcode_utils.stringToInt(line2)
    ret = Solution().hasPathSum(root, sum)

    out = (ret)
    print out
