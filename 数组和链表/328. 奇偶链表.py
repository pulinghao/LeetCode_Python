#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/11/13 10:34 上午
@Author:  pulinghao
@File: 328. 奇偶链表.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass


    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head.next.next
        while slow and fast:
            slownext = slow.next
            fastnext = fast.next
            slow.next = fast
            fast.next = slownext
            slownext.next = fastnext

            slow = slow.next.next
            fast = fastnext.next
        return head


if __name__ == '__main__':
    line = "[1,2,3,4,5]"
    head = leetcode_utils.stringToListNode(line)

    out = Solution().oddEvenList(head)
    str = leetcode_utils.listNodeToString(out)
    print str
