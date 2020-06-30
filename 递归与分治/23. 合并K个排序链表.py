#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/26 6:26 下午
@Author:  pulinghao
@File: 23. 合并K个排序链表.py
@Software: PyCharm
"""

import leetcode_utils

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.lists = []
        pass

    def mergeKLists(self, lists):
        # 分治思想
        self.lists = lists
        length = len(self.lists)
        if length == 0:
            return None
        return self.merge(0,length - 1)
        pass

    def merge(self,left,right):
        if left == right:
            return self.lists[left]

        mid = (left + right) / 2
        left_part = self.merge(left, mid)
        right_part = self.merge(mid + 1, right)
        return self.mergeTwoList(left_part,right_part)

    def mergeTwoList(self,list1,list2):
        if not list2:
            return list1

        if not list1:
            return list2

        p = list1
        q = list2
        res = ListNode(0)
        tail = res
        while p and q:
            if p.val < q.val:
                tail.next = p
                p = p.next
            else:
                tail.next = q
                q = q.next
            tail = tail.next

        if p :
            tail.next = p
        else:
            tail.next = q
        return res.next



        pass


if __name__ == '__main__':
    line = "[]"
    lists = leetcode_utils.stringToListNodeArray(line)

    ret = Solution().mergeKLists(lists)

    out = leetcode_utils.listNodeToString(ret)
    print out 