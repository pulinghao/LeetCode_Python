#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/8/5 12:40 下午
@Author:  pulinghao
@File: 337. 打家劫舍 III.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    class Solution(object):
        def rob(self, root):
            """
            :type root: TreeNode
            :rtype: int

            """

            if not root:
                return 0

            money = root.val

            # 下面存在重复计算！！！
            # 因为孙子节点的值，会被爷爷节点在计算不偷儿子节点的时候，计算一遍（采用偷孙子的方案）
            # 也会被儿子节点，在计算自己的儿子节点时，又计算一遍（采用偷儿子的方案）
            # 也就是说，会被爷爷计算一遍，也会被儿子计算一遍
            if root.left:
                money += self.rob(root.left.left) + self.rob(root.left.right)

            if root.right:
                money += self.rob(root.right.left) + self.rob(root.right.right)

            return max(money, self.rob(root.left) + self.rob(root.right))

        def rob2(self,root):
            def rob(node):
                if not node:
                    return [0,0]

                res = [] # 第一个元素，表示只偷左右孩子的;第二格元素表示，偷自己的和孙子节点的
                # 如果偷左边的
                # leftRes[0] 保存的是，偷了左子树中的孩子节点（相对于当前来说，是孙子节点）
                # leftRes[1] 保存的是，偷了左子树根节点+孙子节点（相对于当前来说，是儿子节点+儿子的孙子节点）
                leftRes = rob(node.left)
                # 如果偷右边的
                rightRes = rob(node.right)
                res.append(max(leftRes[0],leftRes[1]) + max(rightRes[0],rightRes[1]))
                res.append(node.val + leftRes[0] + rightRes[0])
                return res
            ans = rob(root)
            return max(ans[0],ans[1])



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().func(root)

    print out 