#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/12 6:07 下午
 @Author   :pulinghao@baidu.com
 @File     :637. 二叉树的层平均值.py 
 @Description :
"""

import leetcode_utils

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        # 层序遍历
        queue = [root]
        res = []
        while len(queue):
            cnt = len(queue)
            sum = 0.0
            for i in range(len(queue)):  # 当前层的节点数与队列中的节点数相同
                node = queue.pop(0)
                sum += node.val
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(sum/cnt)

        return res


if __name__ == '__main__':
    line = "[3,9,20,15,7]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().averageOfLevels(root)
    out = leetcode_utils.doubleListToString(ret)
    print out