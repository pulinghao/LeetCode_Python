#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/18 11:16 上午
 @Author   :pulinghao@baidu.com
 @File     :109. 有序链表转换二叉搜索树.py 
 @Description :
"""

import leetcode_utils
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # 1.使用快慢指针找到中间节点，然后构造平衡二叉树
        if not head:
            return None

        slow = head
        fast = head
        pre = head

        if not fast.next:
            return TreeNode(head.val)

        while slow.next and fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)

        rightHead = slow.next
        pre.next = None  # 断链
        if head != slow:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rightHead)
        return root


if __name__ == '__main__':
    line = "[-10, -3, 0, 5, 9]"
    head = leetcode_utils.stringToListNode(line)
    tree = Solution().sortedListToBST(head)
    out = leetcode_utils.treeNodeToString(tree)
    print out
