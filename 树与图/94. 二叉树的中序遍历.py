#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/11 5:08 下午
 @Author   :pulinghao@baidu.com
 @File     :94. 二叉树的中序遍历.py 
 @Description :
"""
import leetcode_utils


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right

        return res

        # 方法二：着色法结题
        # 使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
        # 如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
        # 如果遇到的节点为灰色，则将节点的值输出。

    def inorderTraversal2(self, root):
        WHITE, GRAY = 0, 1
        res = []
        stack = [[WHITE,root]]
        while stack:
            color, node = stack.pop()
            if not node: continue
            if color == WHITE:
                stack.append([WHITE,node.right])
                stack.append([GRAY,node])
                stack.append([WHITE,node.left])
            else:
                res.append(node.val)

        return res

    def inorderTraversal3(self, root):
        # 递归方法
        res = []
        def recursive(root):
            if not root:
                return
            recursive(root.left)
            res.append(root.val)
            recursive(root.right)

        recursive(root)
        return res
    pass

if __name__ == '__main__':
    # line = "[2,1,3]"
    # line = "[2,1,3]"
    line = "[1,null,2,3]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().inorderTraversal3(root)

    print ret