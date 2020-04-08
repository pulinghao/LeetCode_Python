#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/4 9:15 下午
 @Author   :pulinghao@baidu.com
 @File     :leetcode_utils.py 
 @Description :
"""

import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



def stringToListNode(input):
    """
    字符串[1,2,3,4]转链表
    :param input:
    :return:
    """

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
    """
    链表转字符串
    :param node:
    :return:
    """

    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"