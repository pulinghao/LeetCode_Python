#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/11 4:20 下午
 @Author   :pulinghao@baidu.com
 @File     :145. 二叉树的后序遍历.py 
 @Description :
"""

import leetcode_utils

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack1 = [root]  # 用于遍历
        stack2 = []      # 用于保存结果的逆序
        res = []

        while stack1:
            cur = stack1.pop()
            if cur:
                stack2.append(cur.val)
                stack1.append(cur.left)
                stack1.append(cur.right)

        while stack2:
            res.append(stack2.pop())

        return res
        pass





if __name__ == '__main__':
    # line = "[2,1,3]"
    # line = "[2,1,3]"
    line = "[1,null,2,3]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().postorderTraversal(root)
    print ret
