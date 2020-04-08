#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/4 10:30 下午
 @Author   :pulinghao@baidu.com
 @File     :19. 删除链表的倒数第N个节点.py 
 @Description :
"""
import leetcode_utils
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 双指针的思路
        # p = head
        # q = head
        # move = 0
        # while p:
        #     if move >= n:
        #         q = q.next
        #     p = p.next
        #     move += 1
        #     pass
        #
        # if move < n:
        #     return None
        # elif move == n:
        #     return head.next
        # else:
        #     if q.next:
        #         q.next = q.next.next
        # return head
        if not head or not head.next:
            return None
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head

if __name__ == '__main__':
    list1 = "[1,2]"
    n = 2
    # list1 = "[]"
    # list2 = "[0]"

    head1 = leetcode_utils.stringToListNode(list1)


    result = Solution().removeNthFromEnd(head1 ,2)
    print leetcode_utils.listNodeToString(result)