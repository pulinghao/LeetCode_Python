#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/4 9:17 下午
 @Author   :pulinghao@baidu.com
 @File     :83. 删除排序链表中的重复元素.py 
 @Description :
"""

import leetcode_utils

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        # while cur:
        #     next = cur.next
        #     while next:
        #         if cur.val == next.val:
        #             next = next.next
        #         else:
        #             cur.next = next
        #             break
        #     if not next:
        #         cur.next = None
        #     cur = cur.next
        #
        # return head

        while cur and cur.next:
            if cur.val == cur.next.val:
                del_pt = cur.next.next
                cur.next = del_pt
            else:
                cur = cur.next
        return head

if __name__ == '__main__':
    list1 = "[1,1,2,3,3]"

    # head2 = lee stringToListNode(list2)
    head = leetcode_utils.stringToListNode(list1)
    result = Solution().deleteDuplicates(head)
    print leetcode_utils.listNodeToString(result)