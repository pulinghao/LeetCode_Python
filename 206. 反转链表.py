#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/4 3:44 下午
 @Author   :pulinghao@baidu.com
 @File     :206. 反转链表.py 
 @Description :
"""

import json

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1.递归思路
        # if head is None or head.next is None:
        #     return head
        #
        # newhead = self.reverseList(head.next)
        # # 改变第二个节点的next指针
        # head.next.next = head
        # head.next = None
        # return newhead
        # 2.遍历的思路
        # if head is None or head.next is None:
        #     return head
        #
        # pre = head
        # cur = head.next
        # next = head.next.next
        #
        # while(cur):
        #     next = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = next
        #
        # head.next = None  #先当前head位置的next置为None
        # head = pre        #再把head移到头部
        # return head

        p = head
        rev = None
        while p:
            temp_rev = rev
            rev = p
            p = p.next
            rev.next = temp_rev

        return rev

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


def main():
    import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')

    # lines = readlines()
    # while True:
    #     try:
    line = "[1,2,3,4,5]"
    head = stringToListNode(line)

    ret = Solution().reverseList(head)

    out = listNodeToString(ret)
    print out
        # except StopIteration:
        #     break


if __name__ == '__main__':
    main()
