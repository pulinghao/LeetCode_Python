#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/26 10:59 上午
 @Author   :pulinghao@baidu.com
 @File     :5474. 好叶子节点对的数量.py 
 @Description :
"""
import leetcode_utils


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = 0
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """

        if not root:
            return 0

        # 每个节点数组里，保存左子树上，所有叶子节点到这个节点的距离；右子树上，所有叶子节点到这个节点的距离
        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [0]

            pathArray = []
            leftPathArray = dfs(node.left)
            rightPathArray = dfs(node.right)

            # 算上这个node，需要加1
            for i in range(len(leftPathArray)):
                leftPathArray[i] = leftPathArray[i] + 1

            for i in range(len(rightPathArray)):
                rightPathArray[i] = rightPathArray[i] + 1

            # 将两个子数组加起来，计算所有节点的距离
            if len(leftPathArray) > 0 and len(rightPathArray) > 0:
                for i in range(len(leftPathArray)):
                    for j in range(len(rightPathArray)):
                        left = leftPathArray[i]
                        right = rightPathArray[j]
                        if left + right <= distance:
                            self.ans += 1
                for i in range(len(leftPathArray)):
                    pathArray.append(leftPathArray[i])
                for j in range(len(rightPathArray)):
                    pathArray.append(rightPathArray[j])
            elif len(leftPathArray) == 0:
                for i in range(len(rightPathArray)):
                    pathArray.append(rightPathArray[i])
            else:
                for i in range(len(leftPathArray)):
                    pathArray.append(leftPathArray[i])

            return pathArray

        dfs(root)
        return self.ans


if __name__ == '__main__':
    root = "[1,84,null,80,61]"
    distance = 2
    tree = leetcode_utils.stringToTreeNode(root)
    print Solution().countPairs(tree, distance)
