#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/29 11:06 下午
 @Author   :pulinghao@baidu.com
 @File     :95. 不同的二叉搜索树 II.py 
 @Description :
"""

import leetcode_utils
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_tree(left,right):
            if left > right:
                # 这里不能取 =，因为如果是等号，意味着当前子树只有一个节点
                return [None]

            res = []

            for i in range(left, right + 1):
                left_trees = generate_tree(left, i - 1)
                right_trees = generate_tree(i + 1, right)

                for l_tree in left_trees:
                    for r_tree in right_trees:
                        tree = TreeNode(i)
                        tree.left = l_tree
                        tree.right = r_tree
                        res.append(tree)

            return res
        return generate_tree(1,n) if n else []

if __name__ == '__main__':
    print Solution().generateTrees(n = 3)