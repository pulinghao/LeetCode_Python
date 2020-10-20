#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/20 10:06 上午
@Author:  pulinghao
@File: 143. 重排链表.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 1.将每个节点存入数组
        array = []
        cur = head
        while cur:
            array.append(cur)
            cur = cur.next

        N = len(array)
        l = 0
        r = N - 1
        while l <= r:
            lnode = array[l]
            rnode = array[r]
            temp = lnode.next
            lnode.next = rnode
            if temp == rnode or lnode == rnode:
                rnode.next = None
            else:
                rnode.next = temp
            l += 1
            r -= 1

        return head








if __name__ == '__main__':
    line = "[1,2,3,4,5,6]"
    head = leetcode_utils.stringToListNode(line)
    Solution().reorderList(head)
    out = leetcode_utils.listNodeToString(head)
    print out
