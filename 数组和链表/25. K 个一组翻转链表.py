#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/16 11:15 上午
 @Author   :pulinghao@baidu.com
 @File     :25. K 个一组翻转链表.py 
 @Description :
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import leetcode_utils
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1.记录一个count
        cur = head
        count = 1
        start = cur
        firstTime = 1
        res = ListNode(0)
        while cur:
            if count < k:
                count += 1
                cur = cur.next
            else:
                count = 1
                newStart = cur.next
                cur.next = None
                newHead = self.reverseWithCommonSpace(start)
                if firstTime == 1:
                    firstTime -= 1
                    res = newHead
                    pre = start
                    start = newStart
                else:
                    pre.next = newHead
                    pre = start
                    start = newStart
                cur = newStart

        pre.next = newStart

        return res

        # 使用常数空间逆序
    def reverseWithCommonSpace(self, head):
        cur = head
        pre = None
        while cur:
            # 保存下个节点
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    # 使用栈逆序
    def reverseNodeWithStack(self, head):
        cur = head
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next

        newhead = stack.pop(-1)
        cur = newhead
        while stack:
            next = stack.pop(-1)
            cur.next = next
            cur = cur.next

        cur.next = None
        return newhead





if __name__ == '__main__':
    line = "[1,2,3,4,5]"
    head = leetcode_utils.stringToListNode(line)
    line = "3"
    k = leetcode_utils.stringToInt(line)

    ret = Solution().reverseKGroup(head, k)

    out = leetcode_utils.listNodeToString(ret)
    print out