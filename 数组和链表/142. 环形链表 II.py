#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/17 11:32 上午
 @Author   :pulinghao@baidu.com
 @File     :142. 环形链表 II.py 
 @Description :
"""

import leetcode_utils

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 快慢指针的思路，找到第一个节点后，慢指针重新找
        if not head or not head.next or not head.next.next:
            return None

        fast = head
        slow = head
        hasCycle = False
        #1. 先确认有环
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = True
                break
        # slow = fast
        if hasCycle:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None

    def constructCircleList(self,head,pos):
        cur = head
        tail = cur
        while cur:
            tail = cur
            cur = cur.next

        count = pos
        cur = head
        while count:
            cur = cur.next
            count -= 1
        tail.next = cur
        return head

if __name__ == '__main__':
    line = "[3,2,0,-4]"
    head = leetcode_utils.stringToListNode(line)
    line = "1"
    pos = leetcode_utils.stringToInt(line)
    head = Solution().constructCircleList(head,pos)
    ret = Solution().detectCycle(head)

    out = leetcode_utils.listNodeToString(ret)
    print out