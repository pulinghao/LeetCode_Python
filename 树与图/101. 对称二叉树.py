#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/14 10:48 下午
 @Author   :pulinghao@baidu.com
 @File     :101. 对称二叉树.py 
 @Description :
"""

import leetcode_utils
import collections
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 1.递归做法
        if not root:
            return True

        return self.symmetric(root.left,root.right)


        # 2.迭代做法

    # 递归做法
    def symmetric(self, ltree, rtree):
        if not ltree and not rtree:
            return True

        if not ltree or not rtree:
            return False

        if ltree and rtree:
            if ltree.val != rtree.val:
                return False
            else:
                if not ltree.left and not ltree.right and not rtree.left and not rtree.right:
                    return True
                else:
                    return self.symmetric(ltree.left, rtree.right) and self.symmetric(ltree.right, rtree.left)
        return False
        pass

    # 迭代方法
    def symmetricIteraion(self,leftT,rightT):
        queue = collections.deque()
        queue.append((leftT,rightT))
        while queue:
            left,right = queue.popleft()
            if not left and not right:
                # 两个节点为空
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.append((left.left,right.right))
            queue.append((left.right,right.left))

        return True


if __name__ == '__main__':
    # line = "[1,2,2,null,3,3]"
    line2 = "[5,4,8,11,null,13,4,7,2,null,null,5,1]"
    root = leetcode_utils.stringToTreeNode(line2)
    line3 = leetcode_utils.treeNodeToString(root)
    print line3
    # ret = Solution().isSymmetric(root)

    # print ret
