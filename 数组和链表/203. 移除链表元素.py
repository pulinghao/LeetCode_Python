#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/25 6:00 下午
@Author:  pulinghao
@File: 203. 移除链表元素.py
@Software: PyCharm
"""

import leetcode_utils

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    class Solution(object):
        def removeElements(self, head, val):
            """
            :type head: ListNode
            :type val: int
            :rtype: ListNode
            """

            cur = head
            pre = ListNode()
            newHead = pre
            pre.next = cur
            while cur:
                if cur.val == val:
                    pre.next = cur.next
                else:
                    pre = cur
                cur = cur.next
            return newHead.next
if __name__ == '__main__':
    line = "[1,2,6,3,4,5,6]"
    root = leetcode_utils.stringToListNode(line)
    val = 6
    out = Solution().removeElements(root,val)

    print out
