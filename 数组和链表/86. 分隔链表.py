#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/3 5:11 下午
 @Author  :pulinghao@baidu.com
 @File     :86. 分隔链表.py
 @Description :
"""
import leetcode_utils
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(0)
        smallHead = small
        large = ListNode(0)
        largeHead = large

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next

            head = head.next

        large.next = None
        small.next = largeHead.next

        return smallHead.next



if __name__ == '__main__':
    line = "[1,4,3,2,5,2]"
    head = leetcode_utils.stringToListNode(line)
    x = 3
    out = Solution().partition(head,x)
    print leetcode_utils.listNodeToString(out)