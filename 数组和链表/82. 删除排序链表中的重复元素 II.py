#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/25 10:54 下午
 @Author  :pulinghao@baidu.com
 @File     :82. 删除排序链表中的重复元素 II.py
 @Description :
"""
import leetcode_utils
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        pre = newHead
        cur = head
        while cur:
            if cur.next and cur.val != cur.next.val:
                pre = cur
                cur = cur.next
            else:
                if cur.next:
                    temp = cur.val
                    while cur:
                        if cur.val == temp:
                            cur = cur.next
                        else:
                            break
                    pre.next = cur
                else:
                    break
        return newHead.next

    # 递归思路
    def RecursiveDeleteDuplicates(self, head):
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            move = head.next
            while move and head.val == move.val:
                move = move.next
            return self.deleteDuplicates(move)
        return head



if __name__ == '__main__':
    headlist = "[1,1,1,2,3]"
    head = leetcode_utils.stringToListNode(headlist)
    outHead = Solution().deleteDuplicates(head)
    outlist = leetcode_utils.listNodeToString(outHead)
    print outlist




