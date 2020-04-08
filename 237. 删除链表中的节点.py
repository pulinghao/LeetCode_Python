#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/5 4:43 下午
 @Author   :pulinghao@baidu.com
 @File     :237. 删除链表中的节点.py 
 @Description :
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import leetcode_utils

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 让这个节点的next指向下个节点
        # 并替换当前这个节点的值
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    list = "[]"
    head1 = leetcode_utils.stringToListNode(list)

    list = Solution.deleteNode(node)