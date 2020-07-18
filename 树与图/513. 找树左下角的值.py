#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/10 6:54 下午
@Author:  pulinghao
@File: 513. 找树左下角的值.py
@Software: PyCharm
"""
import sys
sys.path.append("..")

import leetcode_utils
import sys
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth,value = self.depth(root)
        return value
        pass

    # 递归方法
    def depth(self,node):
        if not node:
            return 0 , sys.maxint

        left_depth, left_value = self.depth(node.left)
        if left_value == sys.maxint:
            left_value = node.val

        right_depth, right_value = self.depth(node.right)
        if right_value == sys.maxint:
            right_value = node.val

        if left_depth >= right_depth:
            return left_depth + 1,left_value
        else:
            return right_depth + 1,right_value

        pass

    # 迭代方法
    def anotherDepth(self,node):
        # 层序遍历

        queue = [node]
        while len(queue):
            cur = queue.pop(0)

            if cur.right:
                queue.append(cur.right)

            if cur.left:
                queue.append(cur.left)
        return cur.val


        pass


if __name__ == '__main__':
    # line = "[2,1,3]"
    # line = "[2,1,3]"
    line = "[1,2,3,4,null,5,6,null,null,7,null,null,null,null,null]"
    root = leetcode_utils.stringToTreeNode(line)
    ret = Solution().findBottomLeftValue(root)
    print ret
    pass