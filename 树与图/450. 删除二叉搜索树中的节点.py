#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/12 9:41 下午
 @Author   :pulinghao@baidu.com
 @File     :450. 删除二叉搜索树中的节点.py 
 @Description :
"""
import leetcode_utils
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMin(self,node):
        # 递归找到最小值
        if not node.left:
            return node

        return self.getMin(node.left)

    def deleteMin(self,node):
        # 删除树上的最小节点
        if not node.left:
            return node.right

        node.left = self.deleteMin(node.left)
        return node

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        # 1.先找到节点
        if root.val == key:
            # 删除操作
            # 让右子树的左叶子成为新的根
            if not root.left:
                return root.right

            elif not root.right:
                return root.left
            else:
                # 找到右子树的最小节点
                newNode = self.getMin(root.right)
                # 删除右子树的最小节点
                newNode.right = self.deleteMin(root.right)
                newNode.left = root.left
                return newNode
            pass
        elif root.val < key:
            # 在右树上删除
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            # 在左树上删除
            root.left = self.deleteNode(root.left, key)
            return root

if __name__ == '__main__':
    line = "[5,3,6,2,4,null,7]"
    key = 3
    root = leetcode_utils.stringToTreeNode(line)
    out = Solution().deleteNode(root,key)
    res = leetcode_utils.treeNodeToString(out)
    print res