#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/27 11:34 下午
 @Author  :pulinghao@baidu.com
 @File     :61. 旋转链表.py
 @Description :
"""


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        # 1.先求链表的长度
        _len = 0
        cur = head
        while cur:
            _len += 1
            cur = cur.next

        # 2.快慢指针
        fast = head
        slow = head
        k = k % _len
        if k == 0: return head
        while k:
            fast = fast.next
            k -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        newHead = slow.next
        slow.next = None
        fast.next = head
        return newHead


