#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/11 3:43 下午
 @Author   :pulinghao@baidu.com
 @File     :144. 二叉树的前序遍历.py 
 @Description :
"""

import leetcode_utils


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 用queue实现迭代算法
        # if not root:
        #     return []
        #
        # # 使用栈来实现
        # stack = [root]
        #
        # # res保存结果
        # res = []
        #
        # # 栈是否为空，来判断树是否遍历完了
        # while stack:
        #     # 把压进去的节点暂存起来
        #     cur = stack.pop()
        #     res.append(cur.val)
        #
        #     # 先压右侧节点
        #     if cur.right:
        #         stack.append(cur.right)
        #
        #     # 再压左侧节点，左侧节点先弹出
        #     if cur.left:
        #         stack.append(cur.left)
        #
        # return res

        # 着色法
        WHITE, GRAY = 0, 1
        res = []
        stack = [[WHITE, root]]
        while stack:
            color, node = stack.pop()
            if not node: continue
            if color == WHITE:
                stack.append([WHITE, node.left])
                stack.append([WHITE, node.right])
                stack.append([GRAY, node])
            else:
                res.append(node.val)

        return res

    def recursive(self, root):
        def preorder(node, res):
            if node:
                res.append(node.val)
                if node.left:
                    preorder(node.left, res)

                if node.right:
                    preorder(node.right, res)

        res = []
        preorder(root, res)
        return res


if __name__ == '__main__':
    # line = "[2,1,3]"
    # line = "[2,1,3]"
    line = "[1,null,2,3]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().recursive(root)
    print leetcode_utils.integerListToString(ret)
    pass
