#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/4 8:48 下午
 @Author   :pulinghao@baidu.com
 @File     :21. 合并两个有序链表.py 
 @Description :
"""
import json

# Definition for singly-linked list.
def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        #
        # result = ListNode(0)
        # r = result
        # p = l1
        # q = l2
        # while p and q:
        #     # if p.val >= q.val:
        #     #     r.val = q.val
        #     #     q = q.next
        #     # else:
        #     #     r.val = p.val
        #     #     p = p.next
        #     # r.next = ListNode(0)
        #     # r = r.next
        #     if p.val >= q.val:
        #         r.next = q
        #         q = q.next
        #     else:
        #         r.next = p
        #         p = p.next
        #     r = r.next
        #
        #     pass
        #
        # if not p:
        #     # r.val = q.val
        #     r.next = q
        # else:
        #     # r.val = p.val
        #     r.next = p
        # return result.next

        newHead = ListNode(0)

        cur = newHead
        p = l1
        q = l2
        while p and q:
            cur = cur.next
            if p.val >= q.val:
                cur = q
                q = q.next
            else:
                cur = p
                p = p.next


            pass
        if not p:
            cur = q
        else:
            cur = p
        return newHead

if __name__ == '__main__':
    list1 = "[1,2,4]"
    list2 = "[1,3,4]"

    # list1 = "[]"
    # list2 = "[0]"

    head1 = stringToListNode(list1)
    head2 = stringToListNode(list2)

    result = Solution().mergeTwoLists(head1,head2)
    print listNodeToString(result)