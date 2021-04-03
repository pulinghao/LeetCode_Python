#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/18 11:41 下午
 @Author  :pulinghao@baidu.com
 @File     :92. 反转链表 II.py
 @Description :
"""

import leetcode_utils

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        cur = head
        last = None
        l = 1
        while cur:
            while cur and l < left:
                last = cur
                cur = cur.next
                l += 1
                continue

            l += 1
            enter = last
            tail = cur
            while cur and l < right:
                last = cur
                cur = cur.next
                # 暂存next
                next = cur.next
                cur.next = last
                last = cur
                cur = next
                l += 1
            next = cur.next
            cur.next = last
            if enter:
                enter.next = cur
            tail.next = next
            break
        return head

    def reverse2(self,head,left,right):
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next
if __name__ == '__main__':
    head = "[1, 2, 3, 4, 5,6]"
    left = 2
    right = 5

    # head = "[3,5]"
    # left = 1
    # right = 2
    link = leetcode_utils.stringToListNode(head)
    outlink = Solution().reverseBetween(link,left,right)
    out = leetcode_utils.listNodeToString(outlink)
    print out

