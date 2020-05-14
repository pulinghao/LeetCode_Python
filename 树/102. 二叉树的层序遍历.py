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

    def levelOrder2(self, root):
        """ 2刷
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while len(queue) > 0:
            n = len(queue)
            row = []
            while n > 0:
                cur = queue.pop(0)
                n -= 1
                row.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(row)

        return res


if __name__ == '__main__':
    line = "[3,9,20,null,null,15,7]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().levelOrder2(root)
    out = leetcode_utils.int2dArrayToString(ret)
    print out