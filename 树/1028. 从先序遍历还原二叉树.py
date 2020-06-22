#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/18 8:12 下午
 @Author   :pulinghao@baidu.com
 @File     :1028. 从先序遍历还原二叉树.py 
 @Description :
"""
import leetcode_utils

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        stack = []
        i = 0
        while i < len(S):
            level = 0  # 所处层级
            while S[i] == '-':
                level += 1
                i += 1

            value = 0  # 节点的值

            while i < len(S) and S[i].isdigit():
                value = value * 10 + ord(S[i]) - ord('0')
                i += 1

            node = TreeNode(value)

            if level == len(stack):
                if len(stack):
                    stack[-1].left = node
            else:
                stack = stack[:level]  # 取到上个节点处（因为是先左，再右）
                stack[-1].right = node

            stack.append(node)

        return stack[0]  # 获取首个节点

if __name__ == '__main__':
    line = "[1-2--3--4-5--6--7]"
    S = leetcode_utils.stringToString(line)

    ret = Solution().recoverFromPreorder(S)

    out = leetcode_utils.treeNodeToString(ret)
    print out
