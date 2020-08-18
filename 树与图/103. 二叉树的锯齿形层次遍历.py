#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/12 10:50 下午
 @Author   :pulinghao@baidu.com
 @File     :103. 二叉树的锯齿形层次遍历.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        queue1 = [root]
        queue2 = []

        dir = True
        res = []
        while queue1:
            temp = []
            while queue1:
                node = queue1.pop(0)
                if node.left:
                    queue2.append(node.left)

                if node.right:
                    queue2.append(node.right)

                temp.append(node.val)
            if dir:
                res.append(temp[:])
            else:
                res.append(temp[::-1])
            dir = not dir
            queue1 = queue2
            queue2 = []

        return res

if __name__ == '__main__':
    line = "[3,9,20,null,null,15,7]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().zigzagLevelOrder(root)
    out = leetcode_utils.int2dArrayToString(ret)
    print out