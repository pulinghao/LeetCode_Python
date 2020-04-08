#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/7 11:48 上午
@Author:  pulinghao
@File: 2. 两数相加.py
@Software: PyCharm
"""

import json
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # p = l1
        # q = l2
        # result = ListNode(0)
        # res = result
        # sign = 0  # 表示进位
        # while p and q:
        #     if sign == 0:
        #         res.val = p.val + q.val
        #     else:
        #         res.val = p.val + q.val + 1
        #
        #     if res.val > 9:
        #         res.val = res.val - 10
        #         sign = 1
        #     else:
        #         sign = 0
        #     p = p.next
        #     q = q.next
        #     if p and q:
        #         next = ListNode(0)
        #         res.next = next
        #         res = res.next
        #
        # if not p and q:
        #     next = ListNode(0)
        #     res.next = next
        #     res = res.next
        #     while q:
        #         if sign == 0:
        #             res.val = q.val
        #         else:
        #             res.val = q.val + 1
        #
        #         if res.val > 9:
        #             res.val = res.val - 10
        #             sign = 1
        #         else:
        #             sign = 0
        #
        #         q = q.next
        #         if q:
        #             next = ListNode(0)
        #             res.next = next
        #             res = res.next
        #
        # if not q and p:
        #     next = ListNode(0)
        #     res.next = next
        #     res = res.next
        #     while p:
        #         if sign == 0:
        #             res.val = p.val
        #         else:
        #             res.val = p.val + 1
        #         if res.val > 9:
        #             res.val = res.val - 10
        #             sign = 1
        #         else:
        #             sign = 0
        #         p = p.next
        #         if p:
        #             next = ListNode(0)
        #             res.next = next
        #             res = res.next
        #
        # if sign == 1:
        #     next = ListNode(1)
        #     res.next = next
        # return result

        # 更加简单的方法
        result = ListNode(0)
        res = result
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + carry
            carry = s//10
            res.next = ListNode(s%10)
            res = res.next
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry > 0:# 还有进位
            res.next = ListNode(1)
        return result.next


if __name__ == '__main__':
    # list1 = "[2,4,3]"
    # list2 = "[5,6,4]"
    list1 = "[2,4]"
    list2 = "[5,6]"
    head1 = stringToListNode(list1)
    head2 = stringToListNode(list2)

    head3 = Solution().addTwoNumbers(head1, head2)
    list3 = listNodeToString(head3)
    print list3