#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/14 12:55 下午
@Author:  pulinghao
@File: 112. 路径总和.py
@Software: PyCharm
"""

import leetcode_utils
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.pathSum(root,sum)

    def pathSum(self, node, sum):
        if not node:
            return False

        if not node.left and not node.right and node.val == sum:
            return True

        if not node.left and not node.right and node.val != sum:
            return False

        val = sum - node.val
        return self.pathSum(node.left, val) or self.pathSum(node.right,val)






if __name__ == '__main__':
    line = "[5,4,8,11,null,13,4,7,2,null,null,null,1]"
    root = leetcode_utils.stringToTreeNode(line)
    line = "22"
    sum = leetcode_utils.stringToInt(line)

    ret = Solution().hasPathSum(root, sum)

    print ret