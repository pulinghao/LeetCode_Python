#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/14 7:51 下午
@Author:  pulinghao
@File: 572. 另一个树的子树.py
@Software: PyCharm
"""

import leetcode_utils

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True

        if not s and t:
            return False

        return self.isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

        pass

    def isSameTree(self,s,t):
        if not s and not t:
            return True

        if not s or not t:
            return False

        if s.val == t.val:
            return self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)

        return False

if __name__ == '__main__':
    line = "[1,1]"
    s = leetcode_utils.stringToTreeNode(line)
    line = "[1]"
    t = leetcode_utils.stringToTreeNode(line)

    ret = Solution().isSubtree(s, t)

    out = (ret)
    print out