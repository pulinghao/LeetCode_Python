#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/13 12:26 上午
 @Author   :pulinghao@baidu.com
 @File     :102. 二叉树的层序遍历.py 
 @Description :
"""

import leetcode_utils
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue1 = [root]
        queue2 = []
        res = []
        while len(queue1):
            temp = []
            while len(queue1):
                node = queue1.pop(0)
                if node:
                    temp.append(node.val)
                    queue2.append(node.left)
                    queue2.append(node.right)
            if len(temp):
                res.append(temp)
            queue1 = queue2
            queue2 = []

        return res


if __name__ == '__main__':
    line = "[3,9,20,null,null,15,7]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().levelOrder(root)
    out = leetcode_utils.int2dArrayToString(ret)
    print out