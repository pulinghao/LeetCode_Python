#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/4 3:03 下午
 @Author   :pulinghao@baidu.com
 @File     :160. 相交链表.py 
 @Description :
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # listA = []
        # listB = []
        # # 1. 先做链表的逆序
        # while headA.next:
        #     value = headA.val
        #     listA.append(value)
        #     headA = headA.next
        #
        # while headB.next:
        #     value = headB.val
        #     listB.append(value)
        #     headB = headB.next
        #
        # listA.reverse()
        # listB.reverse()
        #
        # num = min(len(listA),len(listB))
        # index = -1
        # for i in range(num):
        #     if listA[i] != listB[i]:
        #         index = i
        #         break
        #
        # if index != -1:
        #     return listA[i]
        # else:
        #     return None

        # 两个指针，PA走headA，PB走headB。HeadA走完后，走HeadB;HeadB走完后，走HeadA
        # 如果相等，那么最后必然相遇
        if headA is None or headB is None:
            return None

        pA = headA
        pB = headB
        while pA != pB:
            if pA is None:
                pA = headB
            else:
                pA = pA.next

            if pB is None:
                pB = headA
            else:
                pB = pB.next

        return pA
