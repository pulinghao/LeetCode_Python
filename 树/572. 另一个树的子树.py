#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/14 7:51 下午
@Author:  pulinghao
@File: 572. 另一个树的子树.py
@Software: PyCharm
"""

import leetcode_utils

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        queue = [s]
        while len(queue):
            node = queue.pop(0)

            if not node and not t:
                return True
            elif not node and t:
                return False
            elif node and not t:
                return True


            if node.val == t.val:
                if not node.left and not node.right and not t.left and not t.right:
                    return True
                else:
                    return self.isSubtree(node.left,t.left) and self.isSubtree(node.right,t.right)
            else:
                queue.append(node.left)
                queue.append(node.right)

        pass

if __name__ == '__main__':
    line = "[1,1]"
    s = leetcode_utils.stringToTreeNode(line)
    line = "[1]"
    t = leetcode_utils.stringToTreeNode(line)

    ret = Solution().isSubtree(s, t)

    out = (ret)
    print out