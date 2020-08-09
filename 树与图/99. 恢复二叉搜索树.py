#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/8 11:00 下午
 @Author   :pulinghao@baidu.com
 @File     :99. 恢复二叉搜索树.py 
 @Description : 考察中序遍历
"""
import leetcode_utils

class Solution(object):
    def __init__(self):
        self.pre = None       # 前一个元素
        self.treeNode1 = None # 第一个错误的点
        self.treeNode2 = None # 第二个错误的点

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        中序遍历后，发现 不满足这个条件:前一个元素 < 当前元素 < 下一个元素，即可进行交换（值交换，不需要节点交换）
        """
        self.__inOrderTree(root)
        temp = self.treeNode1.val
        self.treeNode1.val = self.treeNode2.val
        self.treeNode2.val = temp


    def __inOrderTree(self,root):
        if not root:
            return None

        self.__inOrderTree(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.treeNode1:
                self.treeNode1 = self.pre

            # 每次保存当前的元素
            self.treeNode2 = root
        self.pre = root  # 保存了前一个元素
        self.__inOrderTree(root.right)

if __name__ == '__main__':
    line = "[3,1,4,null,null,2]"
    root = leetcode_utils.stringToTreeNode(line)

    Solution().recoverTree(root)
    res = leetcode_utils.treeNodeToString(root)
    print res