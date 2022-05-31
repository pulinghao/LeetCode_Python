#!/usr/bin/env python
# _*_coding:utf-8 _*_
import leetcode_utils

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum_root = abs(self.getSum(root.left) - self.getSum(root.right))
        return sum_root + self.findTilt(root.left) + self.findTilt(root.right)

    def getSum(self,root):
        # 计算所有节点之和
        if not root:
            return 0
        return root.val + self.getSum(root.left) + self.getSum(root.right)
        pass

if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)
    out = Solution().findTilt(root)
    print out