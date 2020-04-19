#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/19 3:26 下午
 @Author   :pulinghao@baidu.com
 @File     :230. 二叉搜索树中第K小的元素.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def __init__(self):
        self.cnt = 0
        self.val = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.isEqual(root,k)
        return self.val

    def isEqual(self,node,k):
        if not node:
            return

        self.isEqual(node.left,k) # 遍历左子节点，找出最小的那个
        self.cnt += 1
        if self.cnt == k:
            self.val = node.val
            return

        self.isEqual(node.right,k) # 遍历右子树
        pass

if __name__ == '__main__':
    line = ""
    root = leetcode_utils.stringToTreeNode(line)
    line = ""
    k = leetcode_utils.stringToInt(line)

    ret = Solution().kthSmallest(root, k)

    out = leetcode_utils.intToString(ret)
    print out