#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/22 10:51 下午
 @Author   :pulinghao@baidu.com
 @File     :199. 二叉树的右视图.py 
 @Description :
"""
import leetcode_utils
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        res = []
        stack = [root]
        stack2 = []
        new = True
        while stack:
            if new:
                res.append(stack[-1].val)
                new = False
            cur = stack.pop(0)

            if cur.left:
                stack2.append(cur.left)
            if cur.right:
                stack2.append(cur.right)

            if len(stack) == 0:
                stack = stack2
                stack2 = []
                new = True
        return res

if __name__ == '__main__':
    line = "[1,2,3,null,5,null,4]"
    root = leetcode_utils.stringToTreeNode(line)

    ret = Solution().rightSideView(root)

    out = leetcode_utils.integerListToString(ret)
    print out